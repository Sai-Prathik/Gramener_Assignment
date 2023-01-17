import requests
from bs4 import BeautifulSoup


def get_content(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.content,"html.parser")
    content = soup.prettify()
    return content
