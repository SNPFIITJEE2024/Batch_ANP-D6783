# wap which provides a menu to the user to select the 2 -d figure(circle, rectangle, square )after selecting the figure user is again asked to prov. the input of corresponding data for the figure after input of corresponding data again provide a menu to select the operation ( i.e. area, perimeter, operation ) and as per operation/data provided by user, display result of user. this task is repeated again and again until user selects the option to exit from that figure.... 

# while figure = [circle, rectangle, square, exit]
# selected_figure = figure
# operation [perimeter, area]
# selected_operation = operation
# if selected_operation = operation[]

# geometry.py
# Module to calculate area and perimeter of 2D shapes

import math

# ---------------- CIRCLE ----------------
def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r


# ---------------- RECTANGLE ----------------
def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)


# ---------------- SQUARE ----------------
def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s


# ---------------- TRIANGLE ----------------
def triangle_area(b, h):
    return 0.5 * b * h

def triangle_perimeter(a, b, c):
    return a + b + c

# #function to calculate perimeter
# def simpleerest_int():
#     #calculate simple interest
#     interest = (principal * rate * time) / 100
#     #return the calculated interest
#     return interest
# #--------------------------------------------------
# #function to calculate compound interest
# def compound_interest(principal, rate, time):
#     #calculate compound interest
#     amount = principal * (pow((1 + rate / 100), time))
#     interest = amount - principal
#     #return the calculated interest
#     return interest

# #to import a module
# import interestcalculator
# #function to calculate simple interest
# #--- main program ---
# principal = float(input("Enter the principal(in Rs) : : "))
# #validate the principal amount
# if principal < 0:
#     exit("Principal amount cannot be negative.")
# #input of rate of interest
# rate = float(input("Enter the rate of interest (in %): "))
# #validate the rate of interest
# if rate < 0:
#     exit("Rate of interest cannot be negative.")
# #input of time period
# time =int(input("Enter the time period (in years): "))
# #validate the time period
# if time < 0:
#     exit("Time period cannot be negative.")
# #---------------------------------------------
# print("---------------------------------------")
# #to calculate simple interest
# si = interestcalculator.simple_interest(principal, rate, time)
# #displaying simple interest
# print("Simple Interest : Rs", si)