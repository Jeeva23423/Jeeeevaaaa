def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]
def main():
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
