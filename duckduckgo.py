from urllib.parse import quote, urlparse
from bs4 import BeautifulSoup
import requests
import re

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

def parse_results(html):
	soup = BeautifulSoup(html, 'html.parser')
	question_ids = []
	for elem in soup.find_all('a', class_="result-link"):
		url_path = urlparse(elem['href']).path
		match = re.match(r'/questions/(\d+)/', url_path)
		if match:
			question_ids.append(match.group(1))
	return question_ids

def build_query(text, site):
	search_text = f"site:{site} {text}"
	safe_text = quote(search_text)
	query = f"{safe_text}&kl=&df="
	return query


def fetch_question_ids(text, site):
	query = build_query(text, site)
	url = SEARCH_URL.format(query=query)
	
	headers = dict(HEADERS)
	headers['Content-Length'] = str(len(query))
	
	html = requests.get(url, headers=HEADERS).text
	return parse_results(html)


def main():
	question_ids = fetch_question_ids("foobar", "stackoverflow.com")
	print(question_ids)

if __name__ == "__main__":
	main()
