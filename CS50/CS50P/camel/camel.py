def snake(str):
    ret = ""
    for s in str:
        if s.isupper():
            ret += "_" + s.lower()
        else:
            ret += s
    return ret

print("snake_case: " + snake(input("camelCase: ")))


