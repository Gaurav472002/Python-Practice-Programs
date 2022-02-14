# with open('currency.txt') as f:
# 	lines = f.readlines()

# currencyDict = {} 
# for line in lines:
# 	parsed = line.split("\t") # split the data on the basis of tab space    
# 	currencyDict[parsed[0]] = parsed[1]

# amount = float(input("Enter amount:\n"))
# print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
# [print(item) for item in currencyDict.keys()]
# currency = input("Please enter one of these values: \n")
# print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")





with open("currency.txt") as f:
    lines=f.readlines()

    currencyDict={} # dictionary that will hold the all currency values where keys will be the name of the Currency
    for line in lines:
        parsed=line.split("\t")  # split the data on the basis of tab space   
        currencyDict[parsed[0]]=parsed[1]

    amount=float(input("Enter The amount you want to convert:"))
    print("ENter the name of the currency to which you want to convert htis amount..  Available options are:\n")
    [print(item) for item in currencyDict.keys()]
    currency=input("Please enter one of these currency values:\n")
    print(f"{amount} INR is equals to {amount*float(currencyDict[currency])} {currency}")
