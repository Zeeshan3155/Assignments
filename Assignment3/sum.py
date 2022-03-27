def sum_all(numbers):
    a = 0
    for i in numbers:
        a+=i
    print(f"Sum of the numbers is:\n{a}")



liss = []
num = input("Enter the number to add:\n")
while num!="" :
    num = int(num)
    liss.append(num)
    num = input("Enter the next number to add or press enter to exit:\n")
print(f"List of numbers is:\n{liss}")
sum_all(liss)