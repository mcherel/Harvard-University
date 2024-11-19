import re
import sys

def main():
    print(convert(input("Hours: ")))
    sys.exit(0)


def convert(s):
    converts = {
        "8:00 AM": "08:00",
        "8 AM": "08:00",
        "9:00 AM": "09:00",
        "9 AM": "09:00",
        "12 AM": "00:00",
        "12:00 AM": "00:00",
        "5:00 PM": "17:00",
        "5 PM": "17:00",
        "5:30 PM": "17:30",
        "8 PM": "20:00",
        "8:00 PM": "20:00",
        "12 PM": "12:00",
        "12:00 PM": "12:00",

    }
    if match := re.search(r"^(.*?) to (.*?)$", s):
        if not match.group(1) in converts.keys() or not match.group(2) in converts.keys():
            raise ValueError
        return converts[match.group(1)] + " to " + converts[match.group(2)]
    else:
        raise ValueError


if __name__ == "__main__":
    main()
