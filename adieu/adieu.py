import inflect
p = inflect.engine()

#container which has a list of words to be joined/to form a sentence
list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print()
        break

#using inflect module to print a grammatically correct sentence
print("Adieu, adieu, to",p.join(list))