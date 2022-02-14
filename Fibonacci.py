# FIBONACCI SERIES 0,1,1,2,3,5,8,13,21,34,55


def recur_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)

def iter_fibo(n):
    prevnum=0
    currentnum=1
    for n in range(1,n):
        prevprevnum=prevnum
        prevnum=currentnum
        currentnum=prevprevnum+prevnum
    return currentnum
if __name__=="__main__":
    num=int(input("Enter the nth term for the Fibonacci Series:"))
    print(recur_fibo(num))
    print(iter_fibo(num))