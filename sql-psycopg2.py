import psycopg2

# connect to "Chinook" Database

connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

#Query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "Artist"')

#Query 2 - get name from "Artist" column
# cursor.execute('SELECT "Name" FROM "Artist"')

#Query 3 - Find Queen from "Artist Table"
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#Query 4 - Select only by "ArtistId" #51 from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#Query 6 - Select all tracks where composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)