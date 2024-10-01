import sys


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(s):
    # All Digits or Numbers
    for i in s:
        if not i.isalnum():
            return False

    l = len(s)

    # From 2 to 6
    if 2 > l or l > 6:
        return False

    # No zero in Plate
    digits = [i for i in s if i.isdigit()]
    if digits and digits[0] == "0":
        return False

    # Firs two digits
    if not s[:2].isalpha():
        return False
    else:
        # No digits in the middle
        digit = False
        for i in range(2, l):
            if s[i].isdigit():
                digit = True
            if digit and s[i].isalpha():
                return False

    return True


if __name__ == "__main__":
    main()

'''
    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”
'''
