#to conncect tables formed from data of json file roster_data.json

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# creating tables User, Member and Course
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# json file is like
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read() # ro read json file
json_data = json.loads(str_data) # read json data from str_data and store in json_data

for entry in json_data: # json data contains list of lists

    name = entry[0] #first tem of list is name so stored in name vairable
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        ( user_id, course_id, role ) )

    conn.commit()

#after running code execute this
    #SELECT User.name,Course.title, Member.role FROM 
    #User JOIN Member JOIN Course 
    #ON User.id = Member.user_id AND Member.course_id = Course.id
    #ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

#this will show two row then execute following command in DB browser; Note keep roster_data.json in same folder

    #SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    #User JOIN Member JOIN Course 
    #ON User.id = Member.user_id AND Member.course_id = Course.id
    #ORDER BY X LIMIT 1;