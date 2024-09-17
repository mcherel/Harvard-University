def main():
    time = input("What time is it ? ")
    converted__time = round(convert(time) * 100)
    if 700 <= converted__time <= 800:
        print("breakfast time")
    if 1200 <= converted__time <= 1300:
        print("lunch time")
    if 1800 <= converted__time <= 1900:
        print("dinner time")


def convert(time):
    t = time.split(":")
    return float(int(t[0]) + int(t[1]) / 60)


if __name__ == "__main__":
    main()
