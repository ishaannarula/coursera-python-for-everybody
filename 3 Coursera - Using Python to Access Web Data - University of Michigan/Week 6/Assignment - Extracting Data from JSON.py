import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")

if len(url) < 1: print("Error")
print("Retrieving", url)

data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")
try:
    js = json.loads(data)
except:
    js = None

lst = js["comments"]

sum = 0
count = 0
for comcount in lst:
    num = float(comcount["count"])
    sum = sum + num
    count = count + 1
print("Count:", count)
print("Sum:", sum)
