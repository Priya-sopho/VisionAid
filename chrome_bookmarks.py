def export():
	import json
	from json import loads
	from os import environ
	from os.path import expanduser
	from platform import system
	from re import match
	from sys import stderr

	#Getting Input File
	if system() == "Darwin":
		input_filename = expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks")
	elif system() == "Linux":
		input_filename = expanduser("~/.config/google-chrome/Default/Bookmarks")
	elif system() == "Windows":
		input_filename = environ["LOCALAPPDATA"] + r"\Google\Chrome\User Data\Default\Bookmarks"
	else:
		print('Your system ("{}") is not recognized. Please specify the input file manually.'.format(system()))
		exit(1)

	try:
		input_file = open(input_filename, 'r')
	except IOError as e:
		if e.errno == 2:
			print("The bookmarks file could not be found in its default location ({}). ".format(e.filename) +
					"Please specify the input file manually.")
			exit(1)

	# Read, convert, and write the bookmarks
	#output_file = open("bookmarks","w+")
	contents = loads(input_file.read())
	contents = contents['roots']['bookmark_bar']['children']
	input_file.close()
	#json.dump(contents,output_file)
	return contents