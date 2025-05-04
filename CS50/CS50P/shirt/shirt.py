import sys
from PIL import Image, ImageOps

# CLI
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Files and exts
i1 = sys.argv[1]
i2 = sys.argv[2]
valid_ext = ("jpg", "jpeg", "png")

# Valid files
if not i1.lower().endswith(valid_ext):
    sys.exit("Invalid input")

elif not i2.lower().endswith(valid_ext):
    sys.exit("Invalid output")

elif i1[i1.rindex("."):] != i2[i2.rindex("."):]:
    sys.exit("Input and output have different extensions")


# Run program
try:
    f1 = Image.open(i1)
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("File not found")

else:
    f1 = ImageOps.fit(f1, size=shirt.size)
    f1.paste(shirt, shirt)
    f1.save(i2)

