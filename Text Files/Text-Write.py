#This program takes in any given file and keeps writing into it until the user wishes to stop

filename=input("Enter filename")
file=open(filename,"w")
ans='yes'
while ans=='yes':
  x=input("Enter line")
  file.write(x+"\n")
  ans=input("Enter \'yes\' if you wish to continue")
file.close()
