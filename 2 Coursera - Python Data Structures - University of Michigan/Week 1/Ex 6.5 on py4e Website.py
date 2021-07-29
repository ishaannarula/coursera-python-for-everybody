text = 'X-DSPAM-Confidence:    0.8475'
pos = text.find('0')
num_str = text[pos:]
num_float = float(num_str)
print(num_float)
