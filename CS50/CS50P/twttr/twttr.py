def main():
    print("Output: " + shorten(input("Input: ")))

def shorten(word):
    return "".join([w for w in word if w.lower() not in "aeiou"])


if __name__ == "__main__":
    main()
