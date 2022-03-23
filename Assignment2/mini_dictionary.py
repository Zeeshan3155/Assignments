dict = {}
strt_chr = input("Enter starting character for your ASCII value dictionary.\n")
stop_chr = input("Enter last character for your ASCII value dictionary.\n")
for i in range(ord(strt_chr),ord(stop_chr)+1):
    a = chr(i)
    b = ord(a)
    dict[a] = b
print(dict)
