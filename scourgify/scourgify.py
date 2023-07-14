#program to modify files

import sys
import csv

def main():

    command_line_argument()

    try:
        temp = []
        #open a read file into a variable
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            #split the column to modify it's content and appending into temporary list
            for row in reader:
                new = row["name"].split(",")
                temp.append({"first": new[1].lstrip(), "last": new[0], "house": row["house"]})
    #if file cannot be opened/does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    #writing the contents of list into file
    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in temp:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

#if arguments not equal to 3 and not a csv file
def command_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line aruguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")


if __name__ == "__main__":
    main()