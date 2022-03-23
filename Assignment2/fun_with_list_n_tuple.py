def second_element(var):
    return var[-1]

print("FUN WITH LIST AND TUPLE\n")
list = [] 
line = input("Enter elements of first tuple seperated by space and then press enter.\n") 
while(line != ''):
	list.append(tuple(line.split())) 
	line = input("Enter the elemets of next tuple or press enter if input is done.\n") 
print(f"The unsorted list is:\n{list}")
list.sort(key=second_element)
print(f"The sorted list is:\n{list}")