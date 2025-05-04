from datetime import date, datetime
import inflect
import sys

def main():
    d = input("Date of Birth: ")
    if (res := convert(d)) != -1:
        print(f"{inflect.engine().number_to_words(res).capitalize().replace(" and ", " ")} minutes")

    else:
        sys.exit("Invalid date")

def convert(date_of_birth) -> int:
    try:
        target = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        today = date.today()

        if today < target:
            raise ValueError

        return int((today - target).total_seconds() / 60)

    except ValueError:
        return -1

if __name__ == "__main__":
    main()
