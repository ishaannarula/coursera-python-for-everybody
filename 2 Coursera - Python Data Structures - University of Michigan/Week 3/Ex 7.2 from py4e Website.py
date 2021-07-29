fname = input('Enter a filename: ')

try:
    fhandle = open(fname)
except:
    print('The filename entered is either invalid or does not exist')
    quit()

count = 0
total = 0
for line in fhandle:
    line_clean = line.rstrip()
    if line_clean.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos_1stspace = line_clean.find(' ')
        extract = line_clean[pos_1stspace:]
        num_str = extract.strip()
        num = float(num_str)
        total = total + num

print('Total: ', total)
print('Count:', count)
print('Average spam confidence:', total/count)
