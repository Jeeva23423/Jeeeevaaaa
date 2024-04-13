def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 < 0 or num2 < 0:
        print("Please enter positive integers.")
    else:
        print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))


if __name__ == "__main__":
    main()
