num = 1
rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for x in range(i):
        print(num, end=" ")
        num += 1
    print()