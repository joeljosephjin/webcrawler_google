from io import BytesIO
import requests
import bs4
from PIL import Image
import urllib.request

res = requests.get('https://www.google.com/')

soup = bs4.BeautifulSoup(res.text, 'lxml')
img = soup.findAll(attrs={"alt":"Google"})
url = 'https://www.google.com' + img[0]['src']

print(url)

with urllib.request.urlopen(url) as u:
    raw_data = u.read()
image = Image.open(BytesIO(raw_data))

image.show()

