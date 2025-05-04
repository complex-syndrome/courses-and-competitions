def main():
    convert(input("What time is it? ").strip())

def convert(time):
    t = time.split()
    if len(t) == 2:
        numeric, meridiam = t
        hour, minute = [int(n) for n in numeric.split(":")]
        if meridiam == "p.m.": hour = hour + 12

    elif len(t) == 1:
        hour, minute = [int(n) for n in t[0].split(":")]

    else: return ""

    time1 = hour + (minute / 60)

    if 7 <= time1 <= 8:
        print("breakfast time")

    elif 12 <= time1 <= 13:
        print("lunch time")

    elif 18 <= time1 <= 19:
        print("dinner time")

    return time1

if __name__ == "__main__":
    main()
