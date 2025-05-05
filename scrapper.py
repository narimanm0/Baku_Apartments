from urllib.request import Request, urlopen

url = "https://bina.az/items/all"
headers = {'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=headers)
page = urlopen(req)
content = page.read()

print(content)