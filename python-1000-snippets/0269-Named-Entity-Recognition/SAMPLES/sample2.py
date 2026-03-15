# sample2.py
# Use simple pattern matching to find emails and URLs in text.

import re


def extract_emails(text):
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)


def extract_urls(text):
    return re.findall(r"https?://[\w\.-/]+", text)


if __name__ == '__main__':
    text = (
        'Contact us at support@example.com or visit https://example.com for more info. '
        'Also check http://openai.com and send feedback to feedback@openai.com.'
    )

    emails = extract_emails(text)
    urls = extract_urls(text)

    print('Emails:', emails)
    print('URLs:', urls)
