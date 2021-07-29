fhandle = open('mbox-short.txt')

count = 0
for line in fhandle:
    if line.startswith('From '):
        count = count + 1
        pieces = line.split()
        print(pieces[1])

print('There were', count, 'lines in the file with From as the first word')
