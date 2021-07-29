fhandle = open('romeo.txt')

list_agg = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if word in list_agg: continue
        list_agg.append(word)

list_agg.sort()
print(list_agg)
