import requests
import time
from bs4 import BeautifulSoup

url = "https://www.newegg.com/?srsltid=AfmBOopouwiE2fOlqybeD08dCePlu1RZyVd439yvxhDGqfUBLpNgQ9rn"

# to avoid sites that blocks BOTS
headers= {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200: print("failed")

requests.get(url, timeout=10)
time.sleep(2)

soup = BeautifulSoup(response.text,   "lxml")


soup.find("h1")
title = soup.find("div", "goods-title")
price = soup.find("div", "goods-price-current")

print(title, price)






