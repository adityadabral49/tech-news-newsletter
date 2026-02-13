from fetch_news import fetch_top_headlines
from newsletter_email import format_news_email, send_newsletter_email


def lambda_handler(event, context):
    articles = fetch_top_headlines()

    if not articles:
        return {
            "statusCode": 500,
            "body": "No news articles found"
        }

    email_body = format_news_email(articles)

    send_newsletter_email("Daily Tech Newsletter", email_body)

    return {
        "statusCode": 200,
        "body": "Newsletter sent successfully!"
    }