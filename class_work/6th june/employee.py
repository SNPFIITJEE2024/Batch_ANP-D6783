## wap to create a dictionary that contains the record of employee where
# employee id is key and salary as value . so find out the total number 
# of employee having salary greater then 30000. Display the list of 
# employees whole salary is below 20000 

dict={}
num = int(input("enter total number of employees : "))
for i in range (num):
    id = int(input("enter employee id : "))
    salary = int(input("enter salary : "))
    while salary < 0 :
        salary= int(input("again enter salary : "))
    else:
        dict[id] = salary
print(dict)
count = 0
lst=[]
for i in dict :
    if dict[i]>30000:
        count+=1
    if dict[i]<20000:
        lst.append(i)

print(f"employees with salary above 30K are {count}")
print(f"the employees with salary less then 20 k are {lst}")