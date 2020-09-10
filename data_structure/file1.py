# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
s = 0
fh = open(fname)
lines = fh.readlines()

for line in lines:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        a = line.find(":")
        x = line[a+1:]
        x = float(x)
        s=s+x

print("Average spam confidence:",s/ count)
