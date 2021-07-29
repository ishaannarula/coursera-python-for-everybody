import re

fhandle = open('regex_sum_400224.txt')

cumul = 0
count = 0
for line in fhandle:
    numlist = re.findall('[0-9]+', line)
#    print(numb)
    for str in numlist:
        num = int(str)
#        print(num)
        cumul = cumul + num
        count = count + 1

print('Sum is', cumul)
print('Count is', count)
