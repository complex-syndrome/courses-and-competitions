import csv, tabulate as t, sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1], "r") as f:
            l = list(csv.reader(f))
            print(t.tabulate(l[1:], headers=l[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
