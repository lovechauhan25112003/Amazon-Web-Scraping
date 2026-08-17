import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd


def get_title(soup):
    try:
        product_title = single_product_soup.find('span', attrs={'id': 'productTitle'}).text.strip()
    except:
        product_title = ""
    return product_title

def get_price(soup):
    try:
        product_price = single_product_soup.find('span', attrs={'class': 'a-offscreen'}).text.strip()
    except:
        product_price = ""
    return product_price

url = 'http://amazon.com/s?k=ear+buds&crid=2CFDRSRCJZ0H7&sprefix=ear+buds+%2Caps%2C672&ref=nb_sb_noss_2'      

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


links = soup.find_all('a',attrs={"a-link-normal s-no-outline"})

links_list = []

#loop to extract link
for link in links:
    links_list.append("https://www.amazon.com"+link.get('href'))



d = {'Title':[], 'Price':[]}

for link in links_list:
    product_page = requests.get(link, headers=headers)
    single_product_soup = BeautifulSoup(product_page.content, 'html.parser')

    d["Title"].append(get_title(single_product_soup))
    d["Price"].append(get_price(single_product_soup))

amazon_data_fram = pd.DataFrame.from_dict(d)
amazon_data_fram['Title'].replace('',np.nan,inplace=True)
amazon_data_fram = amazon_data_fram.dropna(subset=['Title'])
amazon_data_fram.to_csv('Amazon_Data.csv', header=True, index=False)

print(amazon_data_fram)



# print("TITLE:- " , product_title)
# product_price = single_product_soup.find('span', attrs={'class': 'a-offscreen'}).text.strip()
# print("PRICE:- " , product_price)