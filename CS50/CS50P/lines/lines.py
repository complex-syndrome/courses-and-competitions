import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

else:
    try:
        with open(sys.argv[1], "r") as f:
            print(len([line for line in f.readlines() if not (line.strip() == "" or line.strip().startswith("#"))]))

    except FileNotFoundError:
        sys.exit("File does not exist")
