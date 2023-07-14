from pyfiglet import Figlet
import sys
import random

#using figlet module
figlet = Figlet()

#Expects zero or two command-line arguments
if len(sys.argv) == 1:
    arbitrary_font = True
#The first of the two should be -f or --font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    arbitrary_font = False
else:
    sys.exit(1)

try:
    #if the user would like to output text in a specific font.
    if arbitrary_font == False:
        figlet.setFont(font=sys.argv[2])
except:
    print("Invalid usage")
    sys.exit(1)

else:
    #if the user would like to output text in a random font.
    if arbitrary_font == True:
        figlet.setFont(font=random.choice(figlet.getFonts()))


user = input("Input: ")
print("output: ",figlet.renderText(user))