# program to count number of lines of code

import sys

def main():
    #check for command-line arguments
    check_arguments()
    #open file read through, if unable to open file => file does not exist
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:

    #print the number of lines of code, exceptions["#" and "whitespaces"]
    lines_of_code = 0
    for line in lines:
        if (line.lstrip().startswith("#") or line.isspace()) == False:
            lines_of_code += 1

    print(lines_of_code)

#if the user does not specify exactly two command-line argument, or if the specified file’s name does not end in .py
def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()