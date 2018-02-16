#pip install Google-Search-API
"""
 For documentation 
  https://github.com/abenassi/Google-Search-API
"""
from google import google
num_page = 3
search_results = google.search("bitcoin", 1)
for r in search_results:
	print("-------------------------------")
	print(r.description.encode('utf-8'))
