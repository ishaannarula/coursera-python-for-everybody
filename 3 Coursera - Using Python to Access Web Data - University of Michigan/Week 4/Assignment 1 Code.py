import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_400226.html'
uhand = urllib.request.urlopen(url).read()
#print(uhand)
soup = BeautifulSoup(uhand, 'html.parser')

tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])

print(sum)

#Attempted Codes
#for elements in soup:
#    soup.span.text
#    print(soup.span.text)

#lst = list()
#spans = soup('span')
#print(spans)
#for element in spans:
#    print(element)
#    pos1 = element.find(>)
#    pos2 = element.find('<', pos1)
#    print(pos1)
#    print(pos2)
#    break1 = element.split('>')
#    print(break1)
#val = spans.text
#print(val)
