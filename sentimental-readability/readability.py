# TODO
#Readability in python

statement = input("Enter your statement: ")

letters = 0
words = 0
sentence = 0

for i in statement:
    if(i.isalpha()) == True:
        letters = letters + 1

    if (i.isspace()) == True:
        words = words + 1

    if (i == '.' or i == '?' or i == '!'):
        sentence = sentence + 1

words += 1
L = (letters * 100/words)
S = (sentence * 100/words)

#coleman - index to calculate the grade
index = round(0.0588 * (L) - 0.296 * (S) - 15.8)

if index > 16:
    print("Grade 16+")

elif index < 1:
    print("Before Grade 1")

else:
    print(f"Grade {index}")