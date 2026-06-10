'''Program to read complete data at a time from a file.'''
# Open the file in read mode
filev = open('sentences.txt', 'r')
#to check file is open or not
if not filev:
    exit("Error opening the file.")
# Read the entire content of the file
content = filev.read()
#to check file is empty or not
if not content:
    print("The file is empty.")
else:
    print("Content of the file:")
    print(content)
# Close the file
filev.close()