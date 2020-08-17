from duckduckgo import fetch_question_ids
import requests
import re
import textwrap
import curses

QUERY_URL = "https://api.stackexchange.com/2.2/questions/{question_ids}?order={order}&sort={sort}&site={site}&filter={filter}&key={key}"
	
def build_url(question_ids, site):
	url = QUERY_URL.format(
		question_ids=';'.join(question_ids),
		order='desc',
		sort='activity',
		site=site,
		filter='!)rTkraPXxg*xgr03n8Uq', # built from https://api.stackexchange.com/docs/questions-by-ids
		key='AW5L2UbtlbHGP9T5B0KxTg((', # authenticate with key to up quota to 10,000 from 300
	)
	return url

def fetch_questions(text, site, limit=10):
	question_ids = fetch_question_ids(text, site)[:limit]
	url = build_url(question_ids, site)
	
	data = requests.get(url).json()
	return data

def main():
	fetch_questions('how to use groupby python', 'stackoverflow.com')
	
if __name__ == "__main__":
	main()
