def print_half_pyramid(rows):
    for i in range(1, rows + 1):
        print('* ' * i)


rows = (int(input("Enter the number of rows:")))
print_half_pyramid(rows)
