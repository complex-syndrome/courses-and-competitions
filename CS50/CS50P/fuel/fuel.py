def main():
    while True:
        try:
            if (p := convert(input("Fraction: "))) >= 0:
                print(gauge(p))
                break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction: str) -> int:
    x, y = [int(i) for i in fraction.split("/")]
    if y == 0: raise ZeroDivisionError
    if x > y: raise ValueError
    return round(x/y * 100)

def gauge(percentage: int) -> str:
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
