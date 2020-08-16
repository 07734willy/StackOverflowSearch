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
	limit_count = 0
	index = 0
	option_number = 1
	data_list = []
	
	# Loop to pull questions from json data
	while limit_count < 10:
		
		# Pulls true or false from json data for boolean
		answer = data['items'][limit_count]['is_answered']
		
		# Boolean to see if the question has been answered or not
		if answer == True:
			answer_data = "[Answered]"
		else:
			answer_data = " "
		
		print(" ") # Formatting break
		
		# Adding json data to a list of dictionaries for easy retrieval
		data_list.append({'option': option_number, 'score': data['items'][limit_count]['score'], 'answerbool': answer_data, 'title': data['items'][limit_count]['title'], 'question': data['items'][limit_count]['body']})
		
		# Output the option number /score/answered or not/question title
		print(data_list[index]['option'], ")", data_list[index]['score'], data_list[index]['answerbool'], data_list[index]['title'])
		
		# Remove html tags from question body and output with textwrap of 150
		question_data = re.sub("<.*?>", "",'%.350s' % data_list[index]['question'])
		print(textwrap.fill(question_data, width = 150))
		
		print(" ") # Formatting Break
		
		# Count plus 1 on each loop
		option_number += 1
		limit_count += 1
		index += 1
		

def main():
	fetch_questions('how to use groupby python', 'stackoverflow.com')
	
	

if __name__ == "__main__":
	main()
