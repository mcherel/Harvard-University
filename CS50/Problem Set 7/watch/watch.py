import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"\"https?://(?:www\.)?youtu(?:\.be|be\.com)/embed/(.*?)\"", s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(1)
    return None


if __name__ == "__main__":
    main()
