def main():
    camel = input("camelCase: ")
    for i in camel:
        if i.isupper():
           print("_" + i.lower(), end="")
        else:
            print(i, end="")
    print()

if __name__ == "__main__":
    main()