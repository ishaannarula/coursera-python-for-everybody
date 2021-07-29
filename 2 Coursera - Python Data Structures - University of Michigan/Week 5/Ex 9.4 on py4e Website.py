fhandle = open('mbox-short.txt')

hist = dict()
for line in fhandle:
    if not line.startswith('From '): continue
    list = line.split()
    email_add = list[1]
#Check point
#    print(email_add)
    hist[email_add] = hist.get(email_add,0) + 1
#Check point
#print(hist)
maxima = None
max_val = None
for address,count in hist.items():
    if max_val == None or max_val < count:
        max_val = count
        maxima = address

print(maxima, max_val)
