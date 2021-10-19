import xml.etree.ElementTree as ET #to use xml libraries
import sqlite3

conn = sqlite3.connect('trackdb.sqlite') # make trackdb.sqlite database itself
cur = conn.cursor() #connect cursor to database

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# <key>Genre</key><string>Industrial</string>

#defining function to extract key values from dictionary of xml file
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname) #parse xml file i.e. convert it into string
all = stuff.findall('dict/dict/dict') #in the 3rd inner dctionary
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue # passes entry and track if into look up function defined above

    name = lookup(entry, 'Name')
    genre = lookup(entry, 'Genre')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or genre is None or artist is None or album is None  : 
        continue

    print(name, artist,genre, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) #IGNORE means only if not repeated i.e. unique artist name in column
        VALUES ( ? )''', ( artist, ) ) #insert into name column of artist table the real artist name of xml file
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, )) # take the cursor to that row a
    artist_id = cur.fetchone()[0] # and assign that id to artist_id

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

   # ___________________________________________________________________________

# Execute the command below in database browser to join multiple tables

# SELECT Track.title, Artist.name, Album.title, Genre.name 
 #   FROM Track JOIN Genre JOIN Album JOIN Artist 
 ##   ON Track.genre_id = Genre.id and Track.album_id = Album.id 
 #       AND Album.artist_id = Artist.id
 #   ORDER BY Artist.name LIMIT 3'''

# it will display 3 row table in DB browser in the same execution tab