# program to share readable youtube links

import re

def main():
    #enter the url
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe(.)*<\/iframe>$", s):
        match = re.search(r"(http)(s)?:\/\/(www.)?(youtube.com)\/embed\/([a-zA-Z0-9]+)", s)
        if match:
            #breaking down the link into groups
            grouping = match.groups()
            return f"https://youtu.be/{grouping[-1]}"

if __name__ == "__main__":
    main()