fname = input('Enter the file name with .txt in the end: ')
fhand = open(fname)

for line in fhand:
    strip_line = line.strip()
    print(strip_line.upper())

print()    
print('############################################################################')
print()

fname = input('Enter the file name with .txt in the end: ')
fhand = open(fname)
average = 0
count = 0
sum = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        count += 1
        sum += float(line[20:]) 
average = sum / count
print("Average spam confidance:",average)


