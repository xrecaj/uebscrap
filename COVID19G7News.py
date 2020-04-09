# Llibreries Web Scraping
from typing import List, Any

import pandas as pd
import csv
import re
import xlsxwriter

from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import lxml.html
import requests
from urllib.parse import urljoin

# Init Vars
url_init = 'https://en.wikipedia.org/wiki/Ministry_of_Finance'
url_seed = 'https://en.wikipedia.org/'
g7es_list = ["Canada", "Ministry_of_Public_Action_and_Accounts", "Germany", "Italy", "Japan", "HM_Treasury",
             "United_States_Department_of_the_Treasury", "Ministry_of_Economy_and_Enterprise"]


# Functions Declarations

def download_page(URL_INPUT):
    try:
        page = requests.get(URL_INPUT)
        page.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        page = None
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        page = None

    return page.text


def crawl_initsite(page):
    link_queue = []
    for anchor in page.find_all('a', string=re.compile(r"\w+")):
        link_queue.append(urljoin(url_seed, anchor.get('href')))

    return link_queue


def get_wiki_g7_moe_pages(list_of_links):
    moe_list = []
    for moe in list_of_links:
        if any(z in g7es_list for z in re.findall(r"['\w]+", moe)):
            moe_list.append(moe)
    return moe_list


def get_moe_name(page):
    tree = lxml.html.fromstring(page)
    mn=tree.cssselect("#firstHeading")[0]
    return mn.text

def get_moe_website(page):
    tree = lxml.html.fromstring(page)
    mn=tree.cssselect("#firstHeading")[0]
    td = tree.cssselect("#mw-content-text > div > table[class=\"infobox\"] > tbody ")[0]
    for element in td.iter('a'):
        if element.get('rel') == "nofollow":
            return element.get('href')


# main()

# Wikipedia: de la pàgina inicial proporcionada,
# llista de Ministeris d'Economia del món, obtenir només la llista de links
page_init = BeautifulSoup(download_page(url_init), 'html.parser')
wiki_moe_pages = crawl_initsite(page_init)

# Wikipedia: Llista de Links Pagines Wiki de Ministeris d'Economia
# dels països del G-7 i Espanya
g7_moe_links = get_wiki_g7_moe_pages(wiki_moe_pages)

# MOE: Llista de Links Pàgina Oficial de Ministeries d'Economia
# dels països del G-7 i Espanya
g7_moe_websites = []
g7_moe_name = []
for link in g7_moe_links:
    page = download_page(link)
    if page is not None:
        g7_moe_name.append(get_moe_name(page))
        g7_moe_websites.append(get_moe_website(page))

news_links = []
news_brief = []
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

for site, name in zip(g7_moe_websites, g7_moe_name):
    query = "coronavirus+covid-19"
    query = query.replace(' ', '+')
    site_lang=None
    GOOGLE_SEARCH = f'https://google.com/search?q={query}+site:{site}&lr={site_lang}'
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(GOOGLE_SEARCH, headers=headers)
    print(f'NAME:{name} GS:{GOOGLE_SEARCH}')

    print('response:',resp.status_code)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')

        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "moe": name,
                "query" : GOOGLE_SEARCH,
                "titol": title,
                "link": link
            }
            news_links.append(item)

    for g in soup.find_all('div', class_='s'):
        summary=g.find_all('span',class_='st')
        if summary:
            brief=summary[0].text
            dat=None
            dat=g.find_all('span',class_='f')
            if dat:
                dat=dat[0].string
            item = {
                "data": dat,
                'resum': brief
            }
            news_brief.append(item)

print(news_links)

news_results=[[] for i in range(0,len(news_links))]
for i in range(0,len(news_links)):
    z={**news_links[i],**news_brief[i]}
    news_results[i].append(z)

f_title=[]
f_link=[]
f_date=[]
f_brief=[]
f_query=[]
f_moe=[]
for d in news_results:
    f_moe.append(d[0]['moe'])
    f_query.append(d[0]['query'])
    f_title.append(d[0]['titol'])
    f_link.append(d[0]['link'])
    f_date.append(d[0]['data'])
    f_brief.append(d[0]['resum'])

g={'moe':f_moe,'query':f_query,'title':f_title, 'news_link':f_link, 'published_date': f_date,'brief_summary':f_brief}
g7_moe_news = pd.DataFrame(g)
g7_moe_news.to_csv('C:\\Users\\xrecaj\\Google Drive\\UOC\\08 Tipologia i Cicle de Vida de les Dades\\TCVD_PRA01\\G7_moe_news.csv', sep="|", quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8-sig')
print(g7_moe_news)


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('C:\\Users\\xrecaj\\Google Drive\\UOC\\08 Tipologia i Cicle de Vida de les Dades\\TCVD_PRA01\\G7_MOE_NEWS.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for r in g7_moe_news.iterrows():
    worksheet.write(row, col,     r[row]['moe'])
    worksheet.write(row, col + 1, r[row]['query'])
    worksheet.write(row, col + 2, r[row]['title'])
    worksheet.write(row, col + 3, r[row]['news_link'])
    worksheet.write(row, col + 4, r[row]['published_date'])
    worksheet.write(row, col + 5, r[row]['brief_summary'])
    row += 1

# Write a total using a formula.

workbook.close()