def main():
    s = input("Greeting: ").lower().strip()
    print(f"${value(s)}")

def value(s):
    s = s.lower().strip()
    if s[0:5] == 'hello':
        return 0
    if s and s[0] == 'h':
        return 20
    return 100

if __name__ == "__main__":
    main()