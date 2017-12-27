def export():
	from json import loads
	from os import environ
	from os.path import expanduser
	from platform import system
	from re import match
	from sys import stderr

	html_escape_table = {
		"&": "&amp;",
		'"': "&quot;",
		"'": "&#39;",
		">": "&gt;",
		"<": "&lt;",
		}

	output_file_template = """<dl>{bookmark_bar}</dl>

	<dl>{other}</dl>
	"""

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

	def html_for_node(node):
		if 'url' in node:
			return html_for_url_node(node)
		elif 'children' in node:
			return html_for_parent_node(node)
		else:
			return ''

	def html_for_url_node(node):
		if not match("javascript:", node['url']):
			return '<dt><a href="{}">{}</a>\n'.format(sanitize(node['url']), sanitize(node['name']))
		else:
			return ''

	def html_for_parent_node(node):
		return '<dt><h3>{}</h3>\n<dl><p>{}</dl><p>\n'.format(sanitize(node['name']),
				''.join([html_for_node(n) for n in node['children']]))

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
	output_file = open("bookmarks","w+")
	contents = loads(input_file.read())
	input_file.close()

	bookmark_bar = html_for_node(contents['roots']['bookmark_bar'])
	other = html_for_node(contents['roots']['other'])

	output_file.write(output_file_template.format(bookmark_bar=bookmark_bar, other=other))
	output_file.close()
