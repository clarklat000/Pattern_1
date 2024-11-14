# Ask the user for how many rows and store it in a variable called rows
rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):
    for star in range(1, row + 1):
        # Print a * and a space, with end=""
        print("* ", end="")
    print()