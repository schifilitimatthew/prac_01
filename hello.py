# print('Hello world')

birth_month = int(input("Enter your birth month: "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()
