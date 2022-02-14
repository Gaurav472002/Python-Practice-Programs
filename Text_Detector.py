

import os

def istext(filename):
    with open (filename) as f:
        filecontent=f.read()
    if ("Binod" and "BINOD") in filecontent:
        return True
    else:
        return False
if __name__=="__main__":
 
    dir_contents=os.listdir()
    count=0
    for item in dir_contents:
        
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            check=istext(item)
            if check:
                print(f" Binod Found!!!! in {item}")
                count+=1
            else:
                print(f"Binod not found in {item}")
    print(f"{count} files found with the text Binod...")

