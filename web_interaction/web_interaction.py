from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from urllib.parse import urlparse
import re


browser = webdriver.Chrome('path to your web browser executable')


def google_search(query: str = None):
    browser.get('https://google.com')

    assert 'Google' in browser.title

    search_bar = browser.find_element_by_name('q')
    search_bar.clear()
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)


def generic_interaction(website: str = 'https://google.com', element_name: str = 'q', query=None):
    browser.get(website)
    browser.maximize_window()

    finder = ''
    try:
        elem = browser.find_element_by_name(element_name)
    except selenium.common.exceptions.NoSuchElementException:
        try:
            elem = browser.find_element_by_partial_link_text(element_name)
            finder = 'partial_link'
        except selenium.common.exceptions.NoSuchElementException:
            try:
                elem = browser.find_element_by_id(element_name)
                finder = 'id'
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    elem = browser.find_element_by_tag_name(element_name)
                    finder = 'tag'
                except selenium.common.exceptions.NoSuchElementException:
                    try:
                        elem = browser.find_element_by_class_name(element_name)
                        finder = 'class'
                    except selenium.common.exceptions.NoSuchElementException:
                        try:
                            elem = browser.find_element_by_link_text(element_name)
                            finder = 'link'
                        except selenium.common.exceptions.NoSuchElementException:
                            try:
                                elem = browser.find_element_by_css_selector(element_name)
                                finder = 'css'
                            except selenium.common.exceptions.NoSuchElementException:
                                error = 'Could not find that element name!'
                                print(error)
                                raise

    if query is not None:
        elem.send_keys(query)
        elem.send_keys(Keys.RETURN)
    elif finder == 'partial_link':
        elem.click()
    else:
        elem.submit()
    handles = browser.window_handles
    print(handles)
    browser.switch_to.window(handles[1]).close()

def watch_video():
    elem = browser.find_element_by_tag_name("a")
    #browser.switch_to.frame(elem)
    elem.click()

def close_popup_tab(website: str):
    parse = urlparse(website)
    netloc = parse.netloc
    if re.search('%s, %s' % (netloc, browser.title())) is None:
        browser.close()




generic_interaction(website='whatever website you want to visit', element_name='what you think a likely name for the element you want to click on is')
