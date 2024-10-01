def main():
    fuel = input("Fraction: ")
    percent = convert(fuel)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            fuel = fraction.split("/")
            if not(fuel[0].isdigit() and fuel[0].isdigit()):
                raise ValueError
            if fuel[1] == "0":
                raise ZeroDivisionError
            x = int(fuel[0])
            y = int(fuel[1])
            if x > y or len(fuel) != 2:
                fraction = input("Fraction: ")
                continue
            else:
                return round(x / y * 100)
        except (ValueError, IndexError, ZeroDivisionError) as e:
            raise



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()
