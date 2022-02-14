Receipt=[]  # List That will store the input of the users
Bill_Total=0

while(True):
    user_input=input("Enter the Price of your item: or Press Q to Quit:\n")
    if(user_input!='Q' and user_input !='q' ):
        
        
        Bill_Total=Bill_Total+ int(user_input)
        
        print(f"Your total so far is: {Bill_Total}")
        
        Receipt.append(user_input)
       
    else:
        print( "Here is your Receipt\n")

        for index in range(0,len(Receipt)):
            print(f" Item{index+1} -> {Receipt[index]}")  # Logic to print ht elist of the  items
        print(f"\nThanks for using our Store Services your total Bill amount is:{Bill_Total}.. Do visit Again.." )
        break