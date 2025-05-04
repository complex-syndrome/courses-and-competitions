import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1], "r") as f1:
            with open(sys.argv[2], "w") as f2:
                dw = csv.DictWriter(f2, delimiter=',', fieldnames=["first", "last", "house"])
                dw.writeheader()

                for r in csv.DictReader(f1):
                    last, first = r["name"].split(", ")
                    dw.writerow({
                        "last" : last,
                        "first" : first,
                        "house" : r["house"]
                    })


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
