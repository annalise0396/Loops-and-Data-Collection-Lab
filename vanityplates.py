def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # length between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False

    #start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    #first number not 0
    has_seen_digit = False
    for char in s:
        if char.isdigit():
            #first number not 0
            if not has_seen_digit and char == '0':
                return False
            has_seen_digit = True
        elif char.isalpha():
            # letter after digit
            if has_seen_digit:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    main()



