def count(str):
    upper, lower = 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)

c = input("Enter the string:\n")
count(c)