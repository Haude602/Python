import sqlite3
conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts') #remove previos records in DB
cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)')
fname=input('Enter fiename')
if(len(fname)<1):fname='mbox-short.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces=line.split()
    email=pieces[1] #2nd element in file
    cur.execute('SELECT count FROM Counts WHERE email=?',(email,)) # question mark is place holder for email address to prevent SQL injection
    row=cur.fetchone() #gives the information from database
    if row is None: #i.e. if no records in DB
        cur.execute('''INSERT INTO Counts(email,count)
                    VALUES (?,1)''',(email,)) #count start from 1
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE email=?',(email,))
    conn.commit() #in database
sqlstr='SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10' #take only 10
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()
