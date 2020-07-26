from urllib.parse import quote
from bs4 import BeautifulSoup
import requests

SEARCH_URL = "https://duckduckgo.com/lite/?q={query}"

HEADERS = {
	 "Host": "lite.duckduckgo.com",
	 "User-Agent": "Mozilla/5.0 Firefox/78.0",
	 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	 "Accept-Language": "en-US,en;q=0.5",
	 "Referer": "https://lite.duckduckgo.com/",
	 "Content-Type": "application/x-www-form-urlencoded",
	 "Origin": "https://lite.duckduckgo.com",
	 "DNT": "1",
}

class Result(object):
	def __init__(self, link, title, desc):
		self.link = link
		self.title = title.strip()
		self.desc = desc.strip()

	def __repr__(self):
		return f"<Result: {self.link}|{self.title}|{self.desc}>"

def parse_results(html):
	soup = BeautifulSoup(html, 'html.parser')
	results = []
	for elem in soup.find_all('a', class_="result-link"):
		sibling = elem.parent.parent.find_next("tr")
		result = Result(elem['href'], elem.text, sibling.text)
		results.append(result)
	return results

def search(text):
	query = quote(text) + "&kl=&df="
	url = SEARCH_URL.format(query=query)
	
	headers = dict(HEADERS)
	headers['Content-Length'] = str(len(query))
	
	html = requests.get(url, headers=HEADERS).text
	return parse_results(html)


def main():
	results = search("foobar")
	print(results)

if __name__ == "__main__":
	main()
