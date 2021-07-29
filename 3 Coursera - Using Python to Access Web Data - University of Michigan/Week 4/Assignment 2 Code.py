import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

link = input('Enter URL: ')
inputcount = input('Enter count: ')
inputpos = input('Enter position: ')

count1 = 0
while count1 < int(inputcount):
    count1 = count1 + 1
    url = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(url, 'html.parser')
    tags = soup('a')

    count2 = 0
    for tag in tags:
        count2 = count2 + 1
        if count2 is not int(inputpos): continue
        reqlink = tag['href']
        print('Retrieving:',reqlink)
        link = reqlink
