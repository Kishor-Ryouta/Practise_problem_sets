#import title and genres from csv into sqlite database

import csv
import cs50

#create database
open("week1.db", "w").close()
db = cs50.SQL("Sqlite:///week1.db")

#create tables
db.execute("CREATE TABLE shows (id integer, title TEXT NOT NULL, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INTEGER, genre TEXT NO NULL, FOREIGN KEY(show_id) REFERENCES shows(id))")

#open csv file
with open("favorites.csv", "r") as file:

    #create DictReader
    reader = csv.DictReader(file)

    #iterate over csv file
    for row in reader:

        #canonicalize title
        title = row["title"].strip().upper()

        #insert title
        show_id = db.execute("INSERT INTO shows(title) VALUES(?)", title)

        #insert genres
        for genres in row["genres"].split(","):

            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", show_id, genre)