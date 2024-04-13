def case_inverse(string):
    inverted_string = ""
    for char in string:
        if char.isupper():
            inverted_string += char.lower()
        elif char.islower():
            inverted_string += char.upper()
        else:
            inverted_string += char
    return inverted_string

def main():
    user_input = input("Enter a string: ")
    inverted_string = case_inverse(user_input)
    print("Case Inverted String:", inverted_string)

if __name__ == "__main__":
    main()
