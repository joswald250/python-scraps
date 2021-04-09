from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import requests



def play_anime_from_gogo(html_doc: str = 'https://www2.gogoanimes.ai/', show_search: str = 'haikyuu'):
    # goes to the website given (gogoanimes) and searches the links on the homepage for a match to the given
    # show_search and then isolates just the portion of that link that I want to attach to the url.
    homepage = requests.get(html_doc).text
    soup = BeautifulSoup(homepage, 'html.parser')
    videos = soup.find_all("a")
    step1 = ''
    for link in videos:
        if re.search(show_search, str(link), re.IGNORECASE):
            step1 = str(link.get('href'))
            break

    step2 = re.sub('/?', '', step1, 1)

    # attempts to open the website
    url = html_doc + step2


    # new beautiful soup
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, 'html.parser')
    iframes = soup.find_all("iframe")
    for iframe in iframes:
        if re.search(r"<iframe.+" + show_search + ".+iframe>", str(soup), re.IGNORECASE):
            iframe = iframe
            break
        else:
            iframe = ''
    print(iframe)
    source = str(re.search(r'src=".+[/\\&]', str(iframe)))
    print(source)
    stripped = re.sub('src=', source, '')
    print(stripped)




play_anime_from_gogo()
