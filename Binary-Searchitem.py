#Searching for data from a binary file

#For this case, we are taking the scenario of an item, its quantity, and the price per unit

import pickle

def searchitem(f):
    fobj=open(f,"rb")
    itname=input("Enter item name")
    try:
        while True:
            iteml=pickle.load(fobj)
            if itname.upper()==iteml[1]:
                print("Item Code: ",iteml[0])
                print("Item Name:",iteml[1])
                print("Quantity:",iteml[2])
                print("Price Per Unit:",iteml[3])
                print("Amount:",iteml[4])
            else:
                continue            
    except:
        fobj.close() 
