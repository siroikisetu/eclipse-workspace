from urllib.request import urlopen
for line in urlopen('http://moe.hao123.com/'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)