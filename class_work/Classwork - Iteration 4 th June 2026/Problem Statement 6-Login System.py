#A website allows users to log in using a password. The correct password is admin123. Write a prOgram that keeps asking the user to enter the password until the correct password is provided

correct_password = "admin123"
entered_password = str(input("enter your password "))
while entered_password != correct_password:
    print("incorrect login credentials ( password ), access denied, try again")
    entered_password = str(input("access denied, try again with correct password "))
print("password is correct, access approved")