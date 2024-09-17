def main():
    vowels = ("A", "E", "I", "O", "U")
    message = input("Input: ")
    print("Output: ", end="")
    for i in message:
        if i.upper() not in vowels:
            print(i, end="")
    print()


if __name__ == "__main__":
    main()