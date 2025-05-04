from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
all_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(all_fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in all_fonts:
    f = sys.argv[2]

else:
    sys.exit("Invalid command-line arguments.")

figlet.setFont(font=f)

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
