from traceback import print_tb


num1=int(input("ENter the 1st Number:"))
num2=int(input("ENter the 1st Number:"))

n=min(num1,num2)
print(n)

for i in range(1,n):
    if(num1%i==0 and num2%i==0):

        hcf=i
print(f"The HCF of {num1},{num2} is :{hcf}")