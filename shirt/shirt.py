# program to fit photo to a shirt using pillow

import sys
from PIL import Image, ImageOps
import os

def main():

    command_line_argument()

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")
    # open shirt image
    shirt = Image.open("shirt.png")
    # get the size of shirt
    size = shirt.size
    # resize it to image file
    resized = ImageOps.fit(image, size)
    # mask the shirt
    resized.paste(shirt,shirt)
    # saving the final image
    resized.save(sys.argv[2])

def command_line_argument():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few comand-line arguments")
    elif file_extension() == False:
        sys.exit("Input and output have different extensions")

# check for input and output extensions
def file_extension():
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    if ext1[1] == ext2[1]:
        return True
    return False

if __name__ == "__main__":
    main()