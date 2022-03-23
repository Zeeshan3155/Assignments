dict = {}
strt_letter = input("Enter starting letter for your ASCII value dictionary.\n")
stop_letter = input("Enter last letter for your ASCII value dictionary.\n")
for i in range(ord(strt_letter),ord(stop_letter)+1):
    a = chr(i)
    b = ord(a)
    dict[a] = b
print(dict)