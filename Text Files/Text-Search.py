#This program takes in any given file and reads across it to return the lines starting with 'a' or 'A' and also the number of them

filename=input("Enter filename")
file=open(filename,"r")
readfile=file.readlines()
file.close()
count=0
for i in readfile:
  if i[0]=='a' or i[0]=='A':
    print(i)
    count+=1
print("\nNo.of lines starting with A or a=",count)
