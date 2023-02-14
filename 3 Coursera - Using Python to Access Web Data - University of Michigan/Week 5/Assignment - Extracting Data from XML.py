#Import libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#Reading the data in the URL and saving it in a string
URL = input('Enter URL: ')
html = urllib.request.urlopen(URL).read()
tree = ET.fromstring(html)

#Creating a list of sub-trees and extracting required data
lst1 = tree.findall('comments/comment/count')
lst2 = list()
for subtree in lst1:
#    print(subtree.text)
    reqdata = subtree.text
    reqdata_num = float(reqdata)
    lst2.append(reqdata_num)
#print(lst2)
print(sum(lst2))
