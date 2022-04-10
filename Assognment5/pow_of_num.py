class Power:
    def pow(self,x,n):
        if x ==1 or n==1 or x ==0:
            return x

        elif n == 0:
            return 1

        elif n>1:
            count = 0
            value = 1
            while count <n :
                value = value*x
                count+=1
            return value

        elif x == -1:
            if n%2==0:
                return 1
            else:
                return -1

        elif n < 0:
            negative_pow = 1 / self.pow(x,-n)
            return negative_pow


num1,num2 = int(input("Enter the number:\n")),int(input("Enter the nth times the power of the number:\n"))
print(f"Answer is:\n{Power().pow(num1,num2)}")

