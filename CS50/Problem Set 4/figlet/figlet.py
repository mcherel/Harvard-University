import sys
from random import choice
import pyfiglet
# pip install pyfiglet


def main():
    if (len(sys.argv) != 1) and (len(sys.argv) != 3):
        sys.exit("Invalid usage")
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()
    font = None
    if len(sys.argv) == 3:
        if sys.argv[1] != '-f' and  sys.argv[1] != '--font':
            sys.exit("Invalid usage")
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        font = sys.argv[2]
    msg = input("Input: ")
    print(font)
    figlet.setFont(font=font or choice(fonts))
    print(figlet.renderText(msg))


if __name__ == "__main__":
    main()