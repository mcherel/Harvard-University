def main():
    s = input("Greeting: ").lower().strip()
    if s[0] != 'h':
        print('$100')
        return
    i = 0
    pay = 100
    while 'hello'[i]:
        pay -= 20 * s.count('hello'[i])
        i += 1
        if i == len('hello'):
            break
    print(f"${pay if pay > 0 else 0}")

if __name__ == "__main__":
    main()
