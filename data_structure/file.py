
fn=input('enter filename')
try:
    fh=open(fn)
except:
    print('enter right name')
    quit()

lines=fh.readlines()
for line in lines:
    line=line.rstrip()
    print(line.upper())
