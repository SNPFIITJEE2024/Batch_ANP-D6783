


'''programe to input 10 sentences from the the user and write them to a file.'''
# open the file in write mode
file1=open("sentence.txt",'w')
print("enter the 10 sentence")
# loop to get 10 sentence from user
for i in range(10):
    sentence=input()
    # append new line charater to the sentence
    sentence+= '\n'
    #write the sentence to the file
    file1.write(sentence)
    print("..........................................")
print("file contain 10 sentence sucessfully ")
file1.close()