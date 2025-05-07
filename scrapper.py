from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

base_url = "https://bina.az/items/all"
headers = {'User-Agent': 'Mozilla/5.0'}

def get_links_from_base():
    req = Request(base_url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")

    links = []
    for a in soup.find_all("a", class_="slider_controls"):
        links.append(a["href"])
    return links

def main():
    links = get_links_from_base()
    print(links)