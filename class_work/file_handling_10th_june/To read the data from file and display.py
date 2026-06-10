# Classwork : To read the data from file and display the following:
# 1. No. of Vowels in file.
# 2. No. of characters into the file.
# 3. No. of lines into the file.


f1=input("enter the name of source file:")
f2=input("enter the name of destination file:")

text=open(f1,"r")
dest=open(f2,"w")

t=text.read()
dest.write(t)
print("copied succesfully:::")
text.close()
dest.close()