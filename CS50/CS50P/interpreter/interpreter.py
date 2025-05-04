def calc(expr) -> float:
    x, y, z = expr
    x = int(x)
    z = int(z)

    match y:
        case "+":
            return float(x + z)
        case "-":
            return float(x - z)
        case "*":
            return float(x * z)
        case "/":
            return float(x / z)

print(calc(input("Expression: ").strip().split()), end="")
