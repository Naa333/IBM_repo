# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    extraction = line.find('0.8475')
    print(extraction)
    count = count + 1
    print(count, line)