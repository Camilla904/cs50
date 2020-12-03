import csv

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Open CSV file
    with open("shows0.csv", "w") as shows:

        # Create writer
        writer = csv.writer(shows)

        # Write header
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # Iterate over TSV file
        for row in reader:

            # If non-adult TV show
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                # Write row
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
  ----------------------------------------------------             
  import csv

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(tiles, delimiter="\t")

    # Open CSV file
    with open("shows1.csv", "w") as shows:

        # Create writer
        writer = csv.writer(shows)

        # Write header
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # Iterate over TSV file
        for row in reader:

            # If non-adult TV show
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                # If year not missing
                if row["startYear"] != "\\N":

                    # If since 1970
                    if int(row["startYear"]) >= 1970:

                        # Write row
                        writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
                        
 ---------------------------------------------------------
 import csv

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Open CSV file
    with open("shows2.csv", "w") as shows:

        # Create writer
        writer = csv.writer(shows)

        # Write header
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # Iterate over TSV file
        for row in reader:

            # If non-adult TV show
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                # If year not missing
                if row["startYear"] != "\\N":

                    # Remove \N from genres
                    genres = row["genres"] if row["genres"] != "\\N" else None

                    # If since 1970
                    if int(row["startYear"]) >= 1970:

                        # Write row
                        writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], genres])
--------------------------------------------------------
import cs50
import csv

# Create database
open("shows3.db", "w").close()
db = cs50.SQL("sqlite:///shows3.db")

# Create table
db.execute("CREATE TABLE shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV show
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year not missing
            if row["startYear"] != "\\N":

                # If since 1970
                startYear = int(row["startYear"])
                if startYear >= 1970:

                    # Remove \N from genres
                    genres = row["genres"] if row["genres"] != "\\N" else None

                    # Insert show
                    db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)",
                               row["tconst"], row["primaryTitle"], startYear, genres)
--------------------------------------------------------------------------------

import cs50
import csv

# Create database
open("shows4.db", "w").close()
db = cs50.SQL("sqlite:///shows4.db")

# Create tables
db.execute("CREATE TABLE shows (id INT, title TEXT, year NUMERIC, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INT, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV show
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year not missing
            if row["startYear"] != "\\N":

                # If since 1970
                startYear = int(row["startYear"])
                if startYear >= 1970:

                    # Trim prefix from tconst
                    id = int(row["tconst"][2:])

                    # Insert show
                    db.execute("INSERT INTO shows (id, title, year) VALUES(?, ?, ?)", id, row["primaryTitle"], startYear)

                    # Insert genres
                    if row["genres"] != "\\N":
                        for genre in row["genres"].split(","):
                            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)


 
