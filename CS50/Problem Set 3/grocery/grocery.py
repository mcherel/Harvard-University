def main():
    grocery = {}
    while True:
        try:
            item = input().upper()
            if item not in grocery:
                grocery[item] = 1
            else:
                grocery[item] += 1
        except ():
            pass
        except EOFError:
            print()
            for item in sorted(grocery):
                print(grocery[item], item)
            break

if __name__ == "__main__":
    main()