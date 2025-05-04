def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def number_checks(string):
    num_found = False
    for i in range(len(string) - 1):
        s = string[i]

        # Check initial 0
        if not num_found and s == '0': return False

        # Check num in mid
        if s.isdigit():
            num_found = True
            if not string[i+1].isdigit():
                return False

    return True

def is_valid(s):
    return s[:2].isalpha()          \
            and s.isalnum()         \
            and 2 <= len(s) <= 6    \
            and number_checks(s)    \

if __name__ == "__main__":
    main()
