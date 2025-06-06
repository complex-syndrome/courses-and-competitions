def main():
    d = input("How much was the meal? ")
    p = input("What percentage would you like to tip? ")
    tip = dollars_to_float(d) * percent_to_float(p)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$", ""))

def percent_to_float(p):
    return float(p.replace("%", "")) / 100

if __name__ == "__main__":
    main()
