#program to check for pattern in a string
import re

def main():
    print(count(input("Text: ")))


def count(s):
    #Match any character which is not a word character
    text = re.findall(r"\b\W*um\b\W*", s, re.IGNORECASE)
    return len(text)

if __name__ == "__main__":
    main()