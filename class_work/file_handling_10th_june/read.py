'''program to read data line by line'''
#open the file in raed mode
file1 = open('sentences.txt', 'r')
#to check file is ope or not
if not file1:
    exit("error opening file")
    #read 
print("enter 10 sentences: ")
#loop to get 10 sentences from the user
for i in range(10):
    #input of sentence from user
    sentence = input()
    #===================
    #append new line character to the esntence
    sentence += '\n'
    #write the sentence to the file
    file1.write(sentence)
    print("=================")
print("file contains 10 sentences successfully")
file.close()


'''program to read data line by line'''
#open the file in raed mode
file1 = open('sentences.txt', 'r')
#to check file is ope or not
if not file1:
    exit("error opening file")
    #read the 