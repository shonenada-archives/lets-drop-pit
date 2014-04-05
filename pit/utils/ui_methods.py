import re


def remove_html(text):
    text = re.compile(r'<[^>]+>').sub('', text)
    return text


def truncate(text, max_length, no_html=True):
    if no_html:
        text = remove_html(text)
    output = text[:max_length]
    return output
