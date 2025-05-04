def main():
    print(f"${value(input("Greeting: ").strip())}")

def value(greeting):
    greeting = greeting.lower()
    r = 100
    
    if greeting.startswith('hello'): r = 0
    elif greeting.startswith('h'): r = 20
    return r

if __name__ == "__main__":
    main()
