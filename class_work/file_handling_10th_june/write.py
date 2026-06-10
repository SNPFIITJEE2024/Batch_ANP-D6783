'''program to input 10 sent.s frum u and write them to a file'''
#open the file in write mode
file1 = open('sentences.txt', 'w')
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


