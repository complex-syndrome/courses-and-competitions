amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    i = input("Insert Coin: ").strip()
    if i in ("25", "10", "5"): amount -= int(i)
print(f"Change Owed: {-amount}")
