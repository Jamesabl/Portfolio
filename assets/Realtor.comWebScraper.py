import urllib.request
from bs4 import BeautifulSoup as b
import csv




with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    base_url = "https://www.realtor.com/realestateagents/boynton-beach_fl/sort-sold/pg-"
    num = 50
    page_num = str(num)
    url = base_url + page_num
    html = urllib.request.urlopen(url).read()
    soup = b(html, "html.parser")
    for i in range(50):
        for post in soup.findAll("div", {"class": "agent-list-card clearfix"}):
            try:
                phone = post.find("div", {"class": "agent-phone hidden-xs hidden-xxs"})
                name = post.find("div", {"class": "agent-name text-bold"})
                writer.writerow({'Name': name, 'Phone': phone})
            except IndexError:
                continue
        num += 1
        page_num = str(num)
        url = base_url + page_num
        html = urllib.request.urlopen(url).read()
        soup = b(html, "html.parser")               
