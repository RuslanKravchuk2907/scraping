import requests
from bs4 import BeautifulSoup
from time import sleep

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

for count in range(1,8):

    sleep(3)

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml") # parser

    data = soup.find_all("div", class_="w-full rounded border") #all information about a specific product

    for i in data:

        name = i.find("h4").text.replace("\n", "") # name of specific product

        price = i.find("h5").text # price of a specific product

        url_img ="https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid" ).get("src") # link to an image of a specific product

        print(name + "\n" + price + "\n" + url_img + "\n\n")
#print(name)
#print(price)
#print(url_img)
#print(data)