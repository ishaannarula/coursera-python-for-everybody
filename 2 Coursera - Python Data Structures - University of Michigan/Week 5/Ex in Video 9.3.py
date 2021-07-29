fhandle = open('words.txt')

list_agg = list()
for line in fhandle:
    list_perline = line.split()
    list_agg = list_agg + list_perline

hist = dict()
for word in list_agg:
    hist[word] = hist.get(word, 1) + 1

print(hist)
