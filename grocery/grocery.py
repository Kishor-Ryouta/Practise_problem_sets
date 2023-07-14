# loop infinitely
# get input from the user (case insensitive)
# sort the list alphetically
# prefix each line with the number of times the user has inputted them
# break the loop if the user inpputs ctrl - d

grocery = {}
while True:
    try:
        shopping_list = input().upper().strip()
        if shopping_list in grocery:
            grocery[shopping_list] += 1
        else:
            grocery[shopping_list] = 1
    except EOFError:
        for key in sorted(grocery):
            print(grocery[key], key)
        break