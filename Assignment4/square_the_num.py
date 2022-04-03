listt = list(map(int,input("Enter the numbers seperated by commas.\n").split(",")))
print(f"List of numbers:\n{listt}")
print(f"Square of list numbers:\n{list(map(lambda x:x**2,listt))}")