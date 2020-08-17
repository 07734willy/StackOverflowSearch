from textwrap import wrap

ITEM_FORMAT = """\
[{score}] {title}
{desc}"""


def format_question(question):
	score = 3
	title = "How to do thing"
	desc = "just do abc, some really long filler text here" + "here " * 50

	indent = ' ' * 4
	desc = '\n'.join(wrap(desc, width=80, tabsize=4, max_lines=3,
		initial_indent=indent, subsequent_indent=indent))

	text = ITEM_FORMAT.format(score=score, title=title, desc=desc)
	return text

print(format_question(None))
