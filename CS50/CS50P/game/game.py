import random as r

level: int

while True:
    level = input("Level: ")

    try:
        level = int(level)
        if level > 0: break
    except ValueError:
        continue

n = r.randint(1, level)

while True:
    g = input("Guess: ")

    try:
        g = int(g)
        if g > 0: pass
        else: raise ValueError
    except ValueError:
        continue

    if g > n:
        print("Too large!")
    elif g < n:
        print("Too small!")
    else:
        print("Just right!")
        break
