def main():
    exp = input("Expression: ").split()
    x = int(exp[0])
    y = exp[1]
    z = int(exp[2])
    tot = 0
    match y:
        case "+":
            tot = float(x + z)
        case "-":
            tot = float(x - z)
        case "*":
            tot = float(x * z)
        case "/":
            tot = x / z
    print(f"{tot:.1f}")



if __name__ == "__main__":
    main()