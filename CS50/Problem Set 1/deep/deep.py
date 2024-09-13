def main():
    s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    match s.lower().strip():
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()

"""
Here’s how to test your code manually:

    Run your program with python deep.py. Type 42 and press Enter. Your program should output:

    Yes

    Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:

    Yes

    Run your program with python deep.py. Type forty-two and press Enter. Your program should output

    Yes

    Run your program with python deep.py. Type 50 and press Enter. Your program should output

    No

"""
