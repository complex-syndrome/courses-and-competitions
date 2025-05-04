import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if search := re.fullmatch(r"(1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM)", s):
        # Get Values
        start_hour, start_minute, start_meridiam, \
        end_hour, end_minute, end_meridiam = search.groups()

        # Translate values
        start_hour = int(start_hour)
        start_minute = int(start_minute or "0")
        end_hour = int(end_hour)
        end_minute = int(end_minute or "0")

        # 12-hour to 24-hour
        start_hour = convert_meridiams(start_hour, start_meridiam)
        end_hour = convert_meridiams(end_hour, end_meridiam)

        # Format values
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    else:
        raise ValueError

def convert_meridiams(hour: int, meridiam: str) -> int:
    if meridiam == "PM" and hour != 12:
        hour += 12

    elif meridiam == "AM" and hour == 12:
        hour = 0

    return hour


if __name__ == "__main__":
    main()
