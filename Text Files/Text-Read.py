#This program takes in any given file and reads/prints out its information

filename=input("Enter filename")
file=open(filename,"r")
for content in file:
  print(content,end=' ')
file.close()
