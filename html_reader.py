from HTMLParser import HTMLParser
import sys,os

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		print "Encountered some data  :", data
		c = raw_input()
		if(c == 'y'):
			os._exit(1)



f = open(sys.argv[1],'r')
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for line in f.readlines():
	parser.feed(line)
f.close()