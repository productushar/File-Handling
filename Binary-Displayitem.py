#Displaying data from a binary file

#For this case, we are taking the scenario of an item, its quantity, and the price per unit

import pickle

def dispitem(f):
    try:
        fobj=open(f,"rb")
    except:
        print("File not found!")
        return None
    try:
        while True:
            iteml=pickle.load(fobj)
            print("Item Code: ",iteml[0])
            print("Item Name:",iteml[1])
            print("Quantity:",iteml[2])
            print("Price Per Unit:",iteml[3])
            print("Amount:",iteml[4])
    except:
        fobj.close()
