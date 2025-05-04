calories = {
    'apple' : 130,
    'banana' : 110,
    'avocado' : 50,
    'sweet cherries' : 100,
    'kiwifruit' : 90,
    'pear' : 100
}

item = input("Item: ").strip().lower()

if calories.get(item) is not None:
    print(f"Calories: {calories.get(item)}")
