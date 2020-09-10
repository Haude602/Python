

while True:
    fname=input('Enter filename')
    try:
        fh=open(fname)
        break
    except:
        print('Enter valid name of file')
    continue
lines=fh.readlines()
counts=dict()
for line in lines:
    line=line.rstrip()
    if line.startswith('From:'):
        words=line.split()
        for word in words:
            if word == words[1]:
                counts[word]=counts.get(word,0)+1

bigword=None
bigcount=-1
for k,v in counts.items():
    if v>bigcount:
        bigcount = v
        bigword = k
print(bigword,bigcount)


