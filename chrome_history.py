def export():
	import json
	from os import environ
	from os.path import expanduser, join
	from platform import system
	from shutil import copy, rmtree
	import sqlite3
	from sys import stderr
	from tempfile import mkdtemp
	import datetime
	html_escape_table = {
		"&": "&amp;",
		'"': "&quot;",
		"'": "&#39;",
		">": "&gt;",
		"<": "&lt;",
		}

	output_file_template = """{items}\n"""

	def html_escape(text):
		return ''.join(html_escape_table.get(c,c) for c in text)

	def sanitize(string):
		res = ''
		string = html_escape(string)

		for i in range(len(string)):
			if ord(string[i]) > 127:
				res += '&#x{:x};'.format(ord(string[i]))
			else:
				res += string[i]

		return res

	#Get Input File
	if system() == "Darwin":
		input_filename = expanduser("~/Library/Application Support/Google/Chrome/Default/History")
	elif system() == "Linux":
		input_filename = expanduser("~/.config/google-chrome/Default/History")
	elif system() == "Windows":
		input_filename = environ["LOCALAPPDATA"] + r"\Google\Chrome\User Data\Default\History"
	else:
		print('Your system ("{}") is not recognized. Please specify the input file manually.'.format(system()))
		exit(1)

	try:
		input_file = open(input_filename, 'r')
	except IOError as e:
		if e.errno == 2:
			print("The history file could not be found in its default location ({}). ".format(e.filename) +
					"Please specify the input file manually.")
			exit(1)
	else:
		input_file.close()


	# Make a copy of the database, open it, process its contents, and write the
	# output file
	output_file = open("history","w+")
	temp_dir = mkdtemp(prefix='py-chrome-history-')
	copied_file = join(temp_dir, 'History')
	copy(input_filename, copied_file)

	try:
		connection = sqlite3.connect(copied_file)
	except sqlite3.OperationalError:
		print('The file "{}" could not be opened for reading.'.format(input_filename))
		rmtree(temp_dir)
		exit(1)

	curs = connection.cursor()

	try:
		curs.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
	except sqlite3.OperationalError:
		print('There was an error reading data from the file')
		rmtree(temp_dir)
		exit(1)

	items = []
	for row in curs:
		if len(row[1]) > 0:
			converted_last_visit = (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[3])).isoformat()
			# print converted_last_visit
			items.append('url:"{}",name:"{}",visit_count:"{}",last_visit_time:"{}"'.format(sanitize(row[0]), sanitize(row[1]),row[2],converted_last_visit))

	json.dump(items,output_file)
	connection.close()
	output_file.close()

