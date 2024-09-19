def main():
    while True:
        try:
            fuel = input("Fraction: ").split("/")
            percent = int(fuel[0])/int(fuel[1]) * 100
            if percent > 100:
                raise ValueError
            elif percent >= 99:
                print("F")
            elif percent <= 1:
                print("E")
            else:
                print(f'{round(percent)}%')
        except (ValueError, IndexError, ZeroDivisionError):
            pass
        else:
            break

if __name__ == "__main__":
    main()
