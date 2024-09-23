from dateutil import parser

def main():
    while True:
        try:
            dt_string = input("Date: ")
            if parse(dt_string):
                print(parser.parse(dt_string).strftime("%Y-%m-%d"))
                return
        except ValueError:
            pass

def parse(s)->bool:
    if "/" in s:
        date = s.split("/")
        if not (1 <= int(date[0]) <= 12):
            return False
    elif not "," in s:
        return False
    elif s.split(",")[0].split()[0][0].isdigit():
        return False
    return True

if __name__ == "__main__":
    main()