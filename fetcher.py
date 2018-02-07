from bs4 import BeautifulSoup
import urllib.request
import re

#Set browser headers
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

#Request URL using urllib
req = urllib.request.Request('http://wiprodigital.com', headers=headers)

#Read the requested URL
html = urllib.request.urlopen(req).read()

#Create a BeautifulSoup object using the "lxml" parser
soup = BeautifulSoup(html, "lxml")

#This line just means find all the 'a' link tags and list them along with the urls
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):

    #Print all links to a "seed" file that we can use later
    for tag in link:
        print(link.get('href'), file= open("seed.txt","a"))



