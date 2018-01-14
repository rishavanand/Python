import requests
from bs4 import BeautifulSoup
import json

def get_yify_feed():

	"""
	Exatracts feeds from Yify's rss feed including 
	their title, link, date, poster and description
	"""

	# Fetch feed
	url = 'https://yts.am/rss/2017/720p/all/7'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
	html = requests.get(url, headers=headers)
	
	# Extract news
	soup = BeautifulSoup(html.text, 'xml')
	items = soup.findAll('item')
	feeds = {}
	for number, item in enumerate(items):
		feed = {}
		feed['title'] = item.find('title').text
		feed['link'] = item.find('link').text
		feed['date'] = item.find('pubDate').text
		feed['poster'] = item.find('enclosure')['url']
		feed['description'] = item.find('description').text
		feeds[number] = feed

	return feeds

# Save feed to file
feeds = get_yify_feed()
my_file = open('rss_yify.json', 'w')
my_file.write(json.dumps(feeds))
my_file.close()