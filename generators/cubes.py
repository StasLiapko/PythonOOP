def add_html_tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@add_html_tags('b')
def b(text):
    return text

@add_html_tags('span')
def span(text):
    return text

paragraph = span(b("Text"))

print(paragraph)