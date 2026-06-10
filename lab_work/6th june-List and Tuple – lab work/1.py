# '''Problem Statement 
# An online store records orders as: 
# orders = [ 
#     ("Laptop", 55000), 
#     ("Mouse", 800), 
#     ("Keyboard", 1500), 
#     ("Monitor", 12000), 
#     ("Pen Drive", 600) 
# ] 

# Write a program to: 
# • Display all products costing more than ₹1000.  
# • Find the most expensive product.  
# • Calculate the total order value.  
# • Count products costing below ₹1000.'''

orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
]

print("all products costing more then 1000 are :")
exp = orders[0]
total = 0
count = 0
for i in orders:
    total+=i[1]

    if i[1]>exp[1]:
        exp=i

    if i[1] > 1000:
        print(i[0] , end=" ")
    
    else:
        count+=1
    
print("\n")
print(f"the most expensive device is : {exp[0]} \n")
print(f"total order value is : {total} \n")
print(f"produscts lesss then 1000 are : {count}")