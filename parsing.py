import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

for count in range(1,8):

    sleep(3)

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml") # parser

    data = soup.find_all("div", class_="w-full rounded border") #all information about a specific product

    for i in data:

       card_url = "https://scrapingclub.com" + i.find("a").get("href")
       list_card_url.append(card_url)

for card_url in list_card_url:

    response = requests.get(card_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml") # parser

    data = soup.find("div", class_="my-8 w-full rounded border")

    name = data.find("h3", class_="card-title").text

    price = data.find("h4").text

    text = data.find("p", class_ = "card-description").text

    url_img ="https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")

    print(name + "\n" + price + "\n" + text + "\n" + url_img + "\n\n")