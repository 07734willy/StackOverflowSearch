from contextlib import suppress
import textwrap
import re

def format_body(body, line_width, num_lines, indent):
	body_length = (line_width - indent) * num_lines
		
	body = re.sub(r"<.*?>", "", body)
	body = textwrap.shorten(body, body_length) 
	body = textwrap.fill(body, line_width - indent)
	body = textwrap.indent(body, prefix=" "*indent)

	return body

def print_menu(data, line_width, indent=4):
	num_lines = 2

	for idx, item in enumerate(data['items'], 1):
		answered_status = " [Answered]" if item['is_answered'] else ""
		
		score = item['score']
		title = item['title']
		body  = item['body']

		desc = format_body(body, line_width, num_lines, indent)

		text = f"{idx}) {score:+}{answered_status} {title}\n{desc}\n"
		print(text)


def get_selection(data):
	num_options = len(data['items'])
	index = 0

	while not 1 <= index <= num_options:
		with suppress(Exception):
			selection = input(f"Please select an option between 1 and {num_options}: ")
			index = int(selection)
	return index

def main():
	from stackapi import fetch_questions

	questions = fetch_questions('how to use groupby python', 'stackoverflow.com')
	print_menu(questions, 150)
	selection = get_selection(questions)

	print("You chose", selection)


if __name__ == "__main__":
	main()
