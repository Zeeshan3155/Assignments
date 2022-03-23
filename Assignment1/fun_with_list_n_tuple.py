def second_element(var):
    return var[-1]

list = [] 
line = input("Enter elements of first tuple seperated by space and then press enter.\n") 
while(line != ''):
	list.append(tuple(line.split())) 
	line = input("Enter the elemets of next tuple or press enter if input is done.\n") 
list.sort(key=second_element)
print(list)