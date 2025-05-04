import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip) -> bool:
    return '.' in ip \
        and len(ip.split('.')) == 4 \
        and all(i.isdigit() and 0 <= int(i) <= 255 for i in ip.split('.'))


if __name__ == "__main__":
    main()
