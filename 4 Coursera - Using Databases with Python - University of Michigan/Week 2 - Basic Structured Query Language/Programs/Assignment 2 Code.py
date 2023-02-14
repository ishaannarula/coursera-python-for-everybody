import sqlite3

conn = sqlite3.connect('Assignment 2 - Counting Organisations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From: '): continue
    pieces1 = line.split()
    pieces2 = pieces1[1].split('@')
    org = pieces2[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES(?,1)', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), int(row[1]))

cur.close()
