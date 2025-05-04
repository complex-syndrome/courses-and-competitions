import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if search := re.search(r'<iframe[^>]+src="https?://(?:www.)?youtube\.com/embed/([^&?"/]+)">', s):
        return "https://youtu.be/" + search.group(1)

if __name__ == "__main__":
    main()
