fhandle = open('mbox-short.txt')

lst3 = list()
for line in fhandle:
    if not line.startswith('From '): continue
    lst1 = line.split()
    time = lst1[5]
#Checkpoint
#    print(lst[5])
    lst2 = time.split(':')
    hr = lst2[0]
    lst3.append(hr)

#Checkpoint
#print(lst3)

dist = dict()
for hr1 in lst3:
    dist[hr1] = dist.get(hr1, 0) + 1
#Checkpoint
#print(dist)

lst4 = sorted(dist.items())
for key, value in lst4:
    print(key, value)
