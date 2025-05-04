dictionary = dict()

while True:
    try:
        response = input().strip().upper()
        if response != "":
            if dictionary.get(response) is None:
                dictionary[response] = 1
            else:
                dictionary[response] += 1
    except EOFError:
        for key, val in sorted(dictionary.items()):
            print(f"{val} {key}")
        break
