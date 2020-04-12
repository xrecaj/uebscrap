from typing import Dict, List, Any, Union
import os
import pandas as pd
import csv
import re
import lxml.html
import requests

from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.parse import urljoin


#
# Declaració de Funcions
#
def download_page(url_input):
    try:
        page = requests.get(url_input, headers=headers)
        if page.headers['Content-Type'].find("text/html") < 0:
            print(page.headers['Content-Type'])
            return '<NON-TEXT PAGE>' + page.headers['Content-Type']
        else:
            page.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        page = None
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        page = None
    return page.text


def get_wiki_page_moe_links(page):
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
    mn = tree.cssselect("#firstHeading")[0]
    return mn.text


def get_moe_website(page):
    tree = lxml.html.fromstring(page)
    mn = tree.cssselect("#firstHeading")[0]
    td = tree.cssselect("#mw-content-text > div > table[class=\"infobox\"] > tbody ")[0]
    for element in td.iter('a'):
        if element.get('rel') == "nofollow":
            return element.get('href')


# main()

# INIT VARS
url_init = 'https://en.wikipedia.org/wiki/Ministry_of_Finance'
url_seed = 'https://en.wikipedia.org/'
g7es_list = ["Ministry_of_Public_Action_and_Accounts",
             "Germany",
             "Italy",
             "Japan",
             "Ministry_of_Economy_and_Enterprise"]
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

#
# Wikipedia: de la pàgina inicial proporcionada,
# llista de Ministeris d'Economia del món, obtenir només la llista de links
#
page_init = BeautifulSoup(download_page(url_init), 'html.parser')
wiki_moe_pages = get_wiki_page_moe_links(page_init)

#
# Wikipedia: Llista de Links Pagines Wiki de Ministeris d'Economia
# dels països del G-7 i Espanya
#
g7_moe_links = get_wiki_g7_moe_pages(wiki_moe_pages)

#
# MOE: Llista de Links Pàgina Oficial de Ministeries d'Economia
# dels països del G-7 i Espanya
#
g7_moe_websites = []
g7_moe_name = []

for link in g7_moe_links:
    page = download_page(link)
    if page is not None:
        g7_moe_name.append(get_moe_name(page))
        g7_moe_websites.append(get_moe_website(page))

# MOE Link Excepcions:
#   Unió Europea,
#   U.S Department of Commerce,
#   Canada Department of Finance,
#   UK Department for Business
g7_moe_websites.append('https://ec.europa.eu/')
g7_moe_name.append('European Commission')
g7_moe_websites.append('https://www.commerce.gov')
g7_moe_name.append('U.S. Departament of Commerce')
g7_moe_websites.append('https://www.canada.ca/en/department-finance/')
g7_moe_name.append('Department of Finance (Canada)')
g7_moe_websites.append('https://www.gov.uk/business')
g7_moe_name.append('UK Department for Business, Innovation & Skills')

#
# GOOGLE: Cerca de Noticies relacionades amb el Coronavirus, COVID-19
#
news_links = []
news_brief = []

for site, name in zip(g7_moe_websites, g7_moe_name):
    # Preparació de la QUERY
    query = "allintext:coronavirus"
    query = query.replace(' ', '+')
    last_update_period = 'm'
    # Excepció:
    # Obtenir documents en Espanyol només si la web és la del Ministerio de Empresa (docs no traduits)
    if name != "Ministry of Economy (Spain)":
        site_lang = 'lang_en'
    else:
        site_lang = 'lang_es'
    GOOGLE_SEARCH = f'https://google.com/search?q={query}+site:{site}&lr={site_lang}&tbs=qdr:{last_update_period},'
    resp = requests.get(GOOGLE_SEARCH, headers=headers)
    print(f'NAME:{name} GS:{GOOGLE_SEARCH}')

    print('response:', resp.status_code)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    else:
        print(resp.headers)
    # Web Scrap: Obtenir les dades relevants de la pàgina de resultats de Google
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')

        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "moe": name,
                "query": GOOGLE_SEARCH,
                "title": title,
                "link": link
            }
            news_links.append(item)

    for g in soup.find_all('div', class_='s'):
        summary = g.find_all('span', class_='st')
        if summary:
            brief = summary[0].text
            dat = None
            dat = g.find_all('span', class_='f')
            if dat:
                dat = dat[0].string
            item = {
                "data": dat,
                'brief': brief
            }
            news_brief.append(item)

print(news_links)
#
# MOE Pàgines: Navegar a totes les pàgines trobades a la cerca de GOOGLE i obtenir el text de la noticia.
# Excepcions: Només extreu el text de les pàgines HTML.
#             Extracció de text en altres formats de fitxer són marcats amb en tag NON-TEXT FILE .
#
news_text = []
for n in news_links:
    print('url:', n['link'])
    p = download_page(n['link'])
    if p.find('NON-TEXT PAGE') < 0:
        news_page = BeautifulSoup(p, 'html.parser')

        # Eliminar text de scripts i estils
        for script in news_page(["script", "style"]):
            script.extract()  # rip it out

        # Obtenir text només de la secció BODY de la pàgina
        text = news_page.body.get_text()

        # Neteja de dades:
        # Eliminar espais en blanc entre linies
        # Eliminar linies en blanc
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        news_text.append(text.encode('utf-8'))
    else:
        news_text.append('NOT-TEXT PAGE')

news_results = [[] for i in range(0, len(news_links))]
for i in range(0, len(news_links)):
    z = {**news_links[i], **news_brief[i]}
    news_results[i].append(z)

f_title = []
f_link = []
f_date = []
f_brief = []
f_query = []
f_moe = []

for d in news_results:
    f_moe.append(d[0]['moe'])
    f_query.append(d[0]['query'])
    f_title.append(d[0]['title'])
    f_link.append(d[0]['link'])
    f_date.append(d[0]['data'])
    f_brief.append(d[0]['brief'])

#
# Preparació de les dades i creació del dataset en fitxer CSV
#
g = {'moe': f_moe, 'titol': f_title, 'link': f_link, 'data_publicacio': f_date, 'resum': f_brief, 'text': news_text}
g7_moe_news = pd.DataFrame(g)

current_dir = os.path.dirname(__file__)
file_name = "G7_moe_news_detailed.csv"
file_path = os.path.join(current_dir, file_name)

g7_moe_news.to_csv(file_path, sep=",", quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8-sig')
print(g7_moe_news)
