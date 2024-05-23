import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import os

url = "https://baotainguyenmoitruong.vn/moi-truong"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h3", class_="b-grid__title")

data = []

def get_all_paragraphs(url):
    print("Crawling data ...")
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')

    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]

    author = soup.find('span', class_='sc-longform-header-author block-sc-author').get_text(strip=True)
    publish_time = soup.find('span', class_='sc-longform-header-date block-sc-publish-time').get_text(strip=True)

    return paragraph_texts, author, publish_time

num = 1
for title in titles:
    os.system('cls')
    print("Saving data ..." ,num, "post")
    title_text = title.a.text.strip()
    href = title.a["href"]
    paragraphs, author, publish_time = get_all_paragraphs(href)
    data.append([title_text, href, author, publish_time, paragraphs])
    num = num + 1

    
df = pd.DataFrame(data)
df.to_csv("data2.csv", index=False, encoding="utf-16")
print("Saved data to data2.csv, press any key.....")
input()