


a=int(input("ENter the first number:"))
b=int(input("ENter the Second number:"))
Maxnum=max(a,b)
print(Maxnum)

#Loop to check the LCM of the two Numbers

while(True):
    if(Maxnum%a==0 and Maxnum%b==0):
        break
    Maxnum+=1

print(f"The LCM of The two Numbers  {a},{b} is {Maxnum}")