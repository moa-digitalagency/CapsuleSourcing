import re


def format_price(price, currency='EUR'):
    if currency == 'EUR':
        return f"{price:.2f} EUR"
    elif currency == 'MAD':
        return f"{price:.2f} MAD"
    return f"{price:.2f}"


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def truncate_text(text, max_length=100):
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + '...'
