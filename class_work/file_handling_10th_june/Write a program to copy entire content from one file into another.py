#Write a program to copy entire content from one file into another


f1=input("enter the name of source file:")
f2=input("enter the name of destination file:")

text=open(f1,"r")
dest=open(f2,"w")

t=text.read()
dest.write(t)
print("copied succesfully:::")
text.close()
dest.close()