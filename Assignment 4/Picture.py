rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
for rows in range(rows):
    for cols in range(cols):
        print("*", end="")
    print()