from math import factorial


# num= int(input("Enter the Number: "))
# fact=1

# # factorial using for loop
# for i in range(1,num+1):
#     if (num==0 or num ==1):
#         print("The factorial is 1")
#     else:
#         fact=fact*i
# print (fact)

# using while lopp

# num= int(input("Enter the Number: "))
# fact=1

# while(num>0):
#     fact=fact*num
#     num-=1
# print (fact)








    
# # count trailing zeros method 1  but will not work for Factorial of greater numbers
# count=0
# while(fact%10==0):
#     count+=1
#     fact=fact/10 
#     print (fact)
# print(count)


def fact(number):
	if number==0 or number==1:
		return 1
	else:
		return number * fact(number-1)




def findTrailingZeros(n):
	
	if(n < 0):
		return -1

	# Initialize result
	count = 0

	# Keep dividing n by
	# 5 & update Count
	while(n >= 5):
		n = n//5
        
		count += n


	return count



# Driver program
n =125
print(f"Count of trailing 0s in {n}! is", findTrailingZeros(n))

# This code is contributed by Uttam Singh

