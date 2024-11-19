import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    pattern = fr'^({number}\.){{3}}{number}$'
    return re.search(pattern, ip, flags=0) is not None


if __name__ == "__main__":
    main()
