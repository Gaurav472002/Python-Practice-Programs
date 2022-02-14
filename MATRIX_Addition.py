



def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in  range (n):
            inp=int(input("Enter the number:"))
            row.append(inp)
        o.append(row)
    print(*o,sep="\n") # to print the matrices in the right format
    print("\n")
    return o
    


def Sum_MAtrix(a,b):
    sum=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            total=a[i][j] + b[i][j]
            row.append(total)
        sum.append(row)
    print(*sum,sep="\n")
    return sum
m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns:"))

print("Please enter the value of Matrix A")
A=matrix(m,n)
print("Please enter the value of Matrix B")
B=matrix(m,n)


Sum_MAtrix(A,B)





