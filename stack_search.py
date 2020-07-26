import click


def scrape_overflow(query, sources, answers):
    """
    {
        "title": "string",
        "votes": int,
        "answers": [
            {
                "text": "string",
                "votes": int,
                "author": "string",
                "date": "string" or datetime
            }
        ],
        "tags": [
            "string",
            "string"
        ],
        "link": "string",
        "date": "string" or datetime,
        "author": "string"
    }
    """
    return []


@click.command()
@click.argument('query', nargs=-1, required=True)
@click.option('--sources', '--s', default=2, show_default=True, help='Number of questions used')
@click.option('--results', '--r', default=3, show_default=True, help='Number of answers shown per question')
def main(query, sources, results):
    """ A program that find answers from Stacksoverflow """

    print (" ".join(query), sources, results)
    scraped_data = scrape_overflow(" ".join(query), sources, results)

    for question in scraped_data:
        click.echo(f"Question {question}:")
        for answer in question["answers"]:
            click.echo(f"Answer: {answer}")


if __name__ == "__main__":
    main()
