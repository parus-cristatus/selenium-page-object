from urllib.parse import urlparse


def extract_language_path_from_url(url, position):
    parsed_url = urlparse(url)
    path = parsed_url.path
    language = path.split("/")[position]
    return language



