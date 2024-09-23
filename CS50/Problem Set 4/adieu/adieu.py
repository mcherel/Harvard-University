def main():
    persons = []
    while True:
        try:
            person = input("Name: ").title()
            persons.append(person)
        except ():
            pass
        except EOFError:
            print()
            print("Adieu, adieu, to ", end="")
            if len(persons) == 1:
                print(persons[0])
            elif len(persons) == 2:
                print(f"{persons[0]} and {persons[1]}")
            else:
                last = persons.pop()
                before_last = persons.pop()
                for person in persons:
                    print(person + ", ", end="")
                print(before_last + ", and ", end="")
                print(last)
            break

if __name__ == "__main__":
    main()
