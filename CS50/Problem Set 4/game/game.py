import random

def main():
    level = 0
    while True:
        try:
            if level <= 0:
                level = int(input("Level: "))
                number = random.randint(1, level)
            guess = int(input("Guess: "))
            if guess - number < 0:
                print("Too small!")
            elif guess - number > 0:
                print("Too large!")
            else:
                print("Just right!")
                return
        except (TypeError, ValueError):
            pass

if __name__ == "__main__":
    main()
