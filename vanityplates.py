def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False
    #first 2 letters alpha
    if not s[0].isalpha() and s[1].isalpha():
        return False
    #first number - return false if zero
    index = next((i for i, c in enumerate(s) if c.isdigit()), -1)
    if index == "0":
        return False
    
    #no letters after numbers
    

    return True


if __name__ == "__main__":
    main()


