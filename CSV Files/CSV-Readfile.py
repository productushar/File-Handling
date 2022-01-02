#This program reads a CSV file “student.csv” and displays all the details in the given file. It also counts and displays the number of records in the file.

import csv

with open('marks.csv','r',newline='') as outfile:
    cr=csv.reader(outfile)
    counter=0
    for row in cr:
        print(row)
        counter+=1
    print(counter-1)
    
#The number of rows is taken as counter - 1 since the first row would be that of the information contained and not actual relevant data. 
