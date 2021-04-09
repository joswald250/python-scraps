import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import webbrowser

class EmptyError(Exception):
    message = "You didn't input anything!"

url = "https://www.youtube.com/results?search_query="

while True:
    try:
        search = str(input('What would you like to search YouTube for?'))
        if search == '':
            raise EmptyError()
        break
    except EmptyError:
        print(EmptyError.message)

query = urllib.parse.quote(search)

response = urlopen(url + query)
html = response.read()
soup = BeautifulSoup(html, 'lxml')

youtube_code = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href'][9:]

while True:
    try:
        video_choice_answer = str(input("Would you like to choose the video search result? (Y/N)"))
        if video_choice_answer =='':
            raise EmptyError()
        if video_choice_answer.lower() == "yes" or video_choice_answer.lower() == "y":
            song_link = "https://www.youtube.com/results?search_query=" + youtube_code
            break
        else:
            song_link = "https://www.youtube.com/watch?v=" + youtube_code
            break
    except EmptyError:
        print(EmptyError.message)

website = urllib.request.urlopen(song_link)
webbrowser.open(song_link, new = 2)
