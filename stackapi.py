from duckduckgo import fetch_question_ids
import requests

QUERY_URL = "https://api.stackexchange.com/2.2/questions/{question_ids}?order={order}&sort={sort}&site={site}&filter={filter}"

def build_url(question_ids, site):
	url = QUERY_URL.format(
		question_ids=';'.join(question_ids),
		order='desc',
		sort='activity',
		site=site,
		filter='!)rTkraPXxg*xgr03n8Uq', # built from https://api.stackexchange.com/docs/questions-by-ids
	)
	return url

def fetch_questions(text, site, limit=5):
	question_ids = fetch_question_ids(text, site)[:limit]
	url = build_url(question_ids, site)
	print(url)
	data = requests.get(url).json()
	print(data)

def main():
	fetch_questions('how to use groupby python', 'stackoverflow.com')

if __name__ == "__main__":
	main()
