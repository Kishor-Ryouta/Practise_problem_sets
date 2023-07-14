def main():
    twitter = input("type: ")
    short = shorten(twitter)
    print(short)

def shorten(word):
    tweet = ""
    for letter in word:
        list = ["a", "e", "i", "o", "u"]
        if not letter.lower() in list:
            tweet += letter
    return tweet

if __name__ == "__main__":
    main()