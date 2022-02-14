


# Function to form a matrix
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
    



m=int(input("Enter the number of rows--MATRIX A:"))
n=int(input("Enter the number of columns--- MATRIX A:"))
m1=int(input("Enter the number of rows---MATRIX B:"))
n1=int(input("Enter the number of columns --- MATRIX B:"))

print("Please enter the values of Matrix A")
A=matrix(m,n)
print("Please enter the values of Matrix B")
B=matrix(m1,n1)
print("Please enter the values of Matrix C as 0 ")
C=matrix(n,n1) # taking number of rows from A and Number of columns from B

# Function to multiply the matrices

def multiply(a,b,c):
    for i in range(0,len(C)):
        for j in range(0,len(C[0])):
            for k in range(0,len(B)):
                C[i][j]+=A[i][k]* B[k][j]
    print(*C,sep="\n")
    return C


multiply(A,B,C)

