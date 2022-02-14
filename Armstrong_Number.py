n=int(input("Enter the number:"))
sum=0
copy_n=n
power=len(str(n))
while(n>0):
    digit=n%10
    sum+=digit**power
    n=n//10
if(sum==copy_n):
    print(f"{copy_n} is an armstring number..")
else:
    print(f"{copy_n} is not an Armstrong number..")