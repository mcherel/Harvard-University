import random


def main():

    l = get_level()
    chances = 3
    question = 1
    score = 0
    while question <= 10:
        x = generate_integer(l)
        y = generate_integer(l)
        while chances >= 1:
            ans = input(str(x) + " + " + str(y) + " = ")
            try:
                if int(ans) == x + y:
                    score += 1
                    break
                else:
                    chances -= 1
                    print("EEE")
            except ValueError:
                chances -= 1
                print("EEE")
            if chances == 0:
                print(str(x) + " + " + str(y) + " = " + str(x + y))
        chances = 3
        question += 1
    print("Score: " + str(score))


def get_level():
    levels = ["1", "2", "3"]
    while True:
        l = input("Level: ")
        if l in levels:
            return int(l)


def generate_integer(level):
        return random.randint(0 if level == 1 else 10 if level == 2 else 100, (10 ** level - 1))


if __name__ == "__main__":
    main()