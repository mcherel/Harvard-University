def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)

    # From 2 to 6
    if 2 > l or l > 6:
        return False

    # All Digits or Numbers
    if not s.isalnum():
        return False

    # No zero in Plate
    digits = [i for i in s if i.isdigit()]
    if digits and digits[0] == "0":
        return False

    # Firs two digits
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # No digits in th middle
    if l > 3:
        for i in range(3, l):
            if s[i].isalpha() and s[i - 1].isdigit():
                return(False)
    return True


main()

'''

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”
'''
