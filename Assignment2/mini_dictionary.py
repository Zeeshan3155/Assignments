dict = {}
print("MINI DICTIONARY\n")
strt_chr = input("Enter starting character for your ASCII value dictionary.\n")
stop_chr = input("Enter last character for your ASCII value dictionary.\n")
if ord(strt_chr) < ord(stop_chr):
    for i in range(ord(strt_chr),ord(stop_chr)+1):
        a = chr(i)
        b = ord(a)
        dict[a] = b
    print(f"The dictionary is:\n{dict}")
elif ord(strt_chr) > ord(stop_chr):
    for i in range(ord(strt_chr),ord(stop_chr)-1,-1):
        a = chr(i)
        b = ord(a)
        dict[a] = b
    print(f"The dictionary is:\n{dict}")
else:
    print("Enter a valid character")