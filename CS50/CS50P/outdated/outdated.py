months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

invalid = True
while invalid:
    date = input("Date: ")

    try:
        m, d, y = [int(i) for i in date.split("/")]
    except ValueError:

        try:
            m, d, y = date.split(" ")
            d = int(d[:-1])
            y = int(y)

            m = m.capitalize()
            if m in months:
                m = months.index(m) + 1

        except ValueError:
            continue

    if 1 <= d <= 31 and 1 <= m <= 12: invalid = False

print(f"{y}-{m:>02}-{d:>02}")
