# ''' batsman's scores in different matches are stored in a list. 
# scores = [45, 78, 12, 100, 67, 8, 90, 55] 
# Write a program to: 
# • Count half-centuries and centuries.  
# • Find the highest score.  
# • Display all scores below 20.  
# • Calculate the average score.'''

scores = [45, 78, 12, 100, 67, 8, 90, 55] 
cent = 0
halfcent = 0
sum = 0
for i in scores:
    sum += i
    if i==100:
        cent += 1
    elif i>=50:
        halfcent += 1
    elif i<20:
        print(f"scores less then 20 : {i}")

avg = sum/(len(scores))
print("\n")
print(f"half centuries are : {halfcent} \n")
print(f"centuries are : {cent} \n ")
print(f"highest score is : {max(scores)} \n")
print(f"average score is : {avg}")

    