#Adding data onto a binary file

#For this case, we are taking the scenario of an item, its quantity, and the price per unit

import pickle

def additem(f):
    fobj=open(f,"ab")
    for i in range (int(input("NUMBER OF RECORDS TO BE STORED "))):
        itno=int(input("ENTER THE ITEM NUMBER "))
        itname=input("ENTER ITEM NAME")
        qt=int(input("ENTER QUANTITY"))
        ppu=int(input("ENTER PRICE PER UNIT"))
        amt=qt*ppu
        iteml=[itno,itname.upper(),qt,ppu,amt]
        pickle.dump(iteml,fobj)
    fobj.close()
