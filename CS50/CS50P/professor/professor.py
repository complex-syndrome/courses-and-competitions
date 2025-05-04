import random
import sys

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        eq = f"{x} + {y} = "

        for i in range(3):
            try:
                ans = int(input(eq))
                if ans == x+y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

        if i == 2:
            print(eq + str(x + y))


    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            sys.exit(0)



if __name__ == "__main__":
    main()
