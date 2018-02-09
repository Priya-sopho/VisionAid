class news:

	def __init__(self,keyword = None):
		from newsapi import NewsApiClient
		self.newsapi = NewsApiClient(api_key='ae88bd8bd9d248cdbfba80e514599b60')
		self.keyword = keyword

	def sports(self):
		sports = self.newsapi.get_everything(q='sports',sources='google-news' ,sort_by='relevancy',page = 1)
		return sports
	def politics(self):
		politics = self.newsapi.get_everything(q='politics',sources='google-news-in' ,sort_by='publishedat',page = 1)
		return politics
	def government(self):
		government = self.newsapi.get_everything(q='government',sources='the-hindu' ,sort_by='relevancy',page = 1)
		return sports
	def business(self):
		business = self.newsapi.get_everything(q='business',sources='the-hindu' ,sort_by='relevancy',page = 1)
		return sports
	def keywordNews(self):
		news = self.newsapi.get_everything(q=self.keyword,sources='google-news' ,sort_by='relevancy',page = 1)
		return news


#if user want to search a keyword
news = news('bitcoin')
print news.sports()
