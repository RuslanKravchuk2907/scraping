import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("div", class_="w-full rounded border")

name = data.find("div", class_="p-4")

print(name)