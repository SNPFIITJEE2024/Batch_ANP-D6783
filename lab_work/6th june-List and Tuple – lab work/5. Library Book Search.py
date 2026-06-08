# '''5. Library Book Search 
# Problem Statement 
# Books available in a library: 
# books = [ 
#     ("Python Basics", 5), 
#     ("Data Science", 0), 
#     ("Java Programming", 3), 
#     ("Machine Learning", 0) 
# ] 
# Write a program to: 
# • Display unavailable books.  
# • Find all books with more than 2 copies.  
# • Count available books.  
# • Stop searching once a requested book is found.'''  

books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
count = 0
print("unavailable books are :")

for i in books:
    if i[1]==0:
        print(f"{i[0]}")
    else:
        count+=1

print("\nbooks having more then 2 copies are :")

for i in books :
        if i[1] > 2:
            print(f"{i[0]}")


print(f"\ntotal available books are {count}")

name = input("enter the book you want to find : ")

found = False

for i in books:
    
    if i[0]==name:
        print("book found")
        found = True 
        break

if found == False:
     print("book not found")