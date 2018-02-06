#pip install newsapi-python
import win32com.client as wincl
import os 
sense = wincl.Dispatch("SAPI.SpVoice")

class news:

	def __init__(self,keyword = None):
		from newsapi import NewsApiClient
		self.newsapi = NewsApiClient(api_key='ae88bd8bd9d248cdbfba80e514599b60')
		self.keyword = keyword

	def sports(self):
		sports = self.newsapi.get_everything(q='sports',sources='the-hindu',sort_by='relevancy',page = 1)
		return sports
	def politics(self):
		politics = self.newsapi.get_everything(q='politics',sources='the-hindu' ,sort_by='relevancy',page = 1)
		return politics
	def government(self):
		government = self.newsapi.get_everything(q='government',sources='the-hindu' ,sort_by='relevancy',page = 1)
		return government
	def business(self):
		business = self.newsapi.get_everything(q='business',sources='the-hindu' ,sort_by='relevancy',page = 1)
		return sports
	def keywordNews(self):
		news = self.newsapi.get_everything(q=self.keyword,sources='the-hindu' ,sort_by='relevancy',page = 1)
		return news


def main():
	News = news()
	data = News.government()
	data = data['articles']
	for article in data:
		title = article['title'].encode('ascii','ignore')
		url = article['url'].encode('ascii','ignore')
		desc = article['description'].encode('ascii','ignore')
		sense.Speak('Title'+title)
		sense.Speak('Desciption'+desc)
		sense.Speak('Wanna Listen complete news (yes or no)')
		i = raw_input()
		if(i == 'y'):
			#browse
			pass
		elif(i != 'n'): #if pressed anything else
			os._exit(1)	


if __name__ == '__main__':
	main()