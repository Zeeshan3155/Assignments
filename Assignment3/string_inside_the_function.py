def reverse(string):
    str = ""
    for i in string:
        str = i +str
    return str

strng = input("Enter the string:\n")
print(f"Reversed string is:\n{reverse(strng)}")