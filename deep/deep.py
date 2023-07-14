#user input
deep = input("what is the Answer to the Great Question Of Life? " ).lower().strip()

list = {'forty-two', 'forty two', '42'}
#checking for availability
if (deep in list):
    print('yes')

else:
    print('No')