#This program takes input of the number of records (and relevant information for each record) the user wishes to enter and then writes them into a file named "ITEM.CSV"

import csv

n=int(input('Enter number of records you wish to enter'))
with open('item.csv','w',newline='') as outfile:
    cw=csv.writer(outfile,delimiter=',')
    for i in range(n):
        itcode=int(input("Enter itemcode"))
        descrp=input('Enter Description')
        price=int(input("Enter price"))
        l=[itcode,descrp,price]
        cw.writerow(l)
