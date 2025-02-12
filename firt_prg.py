import secon_prg
import os
import shutil

# print("Hello from the file python")
# type conversion
# num1=39
# num2=45.78
# add = num1+num2
# print("The sum of the two numbers is", add)
# print("The type of the number is",type(add))
#Addition of the string and int
# num1=45
# num2='45'
# sum = num1+int(num2)
# print("The sum of the two numbers is", sum)
#Output formatting

#Traceback (most recent call last):
 # Area of a rectangle

# length = 10
# width = 5
# area = length * width
# print("The area of the rectangle is", area)
# # Area of a circle
# radius = 5
# pi = 3.14
# area = pi * radius ** 2
# print("The area of the circle is", area)
# # Area of a triangle
# base =89
# height=90
# area =1/2*(base*height)
# print("The area of the triangle is", area) 
# #Area of triangle using input
# base=int(input("Enter the base of the triangle: ")) 
# height=int(input("Enter the height of the triangle: ")) 
# area =1/2*(base*height) 
# print("The area of the triangle is", area)
#  # check odd and even number
# num =int(input("Enter a number:"))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# check the greatest amon three numbers
# num1= int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))
# if num1>num2 and num1>num3:
#     print("The greatest number is", num1)
# elif num2>num1 and num2>num3:
#     print("The greatest number is ", num2)
# else:
#     print("The greatest number is ", num3)  

#for loop
# exp=[100,200,300,400,500]
# total=0  
# for i in exp:
#     total=total+i
#     print("The total of the expenses is", total)    
#print the sum of the first 10 numbers
# total=0
# for i in range(1,11):
#     total=total+i
#     print("The total of the first 10 numbers is", total)

# check whether the number is neagative or non negative
# num =int(input("Enter a number: "))
# if num>0:
#     print("The given number is non negative")
# else:
#     print("The given number is negative")
# iterate from i = 0 to 3
# for _ in range(0, 4):
#     print('Hi')
    #Python while Loop
# number = 1
# while number <= 3:
#     print(number)
#     number = number + 1

# Print numbers until the user enters 0
# number = int(input('Enter a number: '))

# # iterate until the user enters 0
# while number != 0:
#     print(f'You entered {number}.')
#     number = int(input('Enter a number: '))

# print('The end.')
# age = 32

# # The test condition is always True
# while age > 18:
#     print('You can vote')
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# n = 10
# # use pass inside if statement
# if n > 10:
#     print("THe hello world")
#     pass
# print('Hello')

# Create a Function
# def greet():
#     print('Hello World!')
# greet()
# function to add 
# def add(num1,num2):
#     sum=num1+num2
#     return sum
# print(add(4,66))
#switch or match case in python
# def calculate(a,b,operation):
#     match operation:
#         case "+":
#             return a+b
#         case "-":
#             return a-b
#         case "*":
#             return a*b
#         case "/":
#             return a / b if b != 0 else "Cannot divide by zero"
#         case _:
#             return "Invalid calculation"
        
# a, b = 10, 5.5
# operation = '/'
# result = calculate(a, b, operation)
# print(f"Result: {result}")

# Recursion in Python
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))   
# num=4
# print("The factorial of the given nmber is",factorial(num))
#using the function from the second program
# print(secon_prg.add(9,6))
# print(dir(secon_prg))
# import math
# print(math.pi)
# print(__name__)
# def main():
#     print("Hello World")

# if __name__=="__main__":
#     main()
# print(os.mkdir('third_prg'))
# shutil.rmtree("third_prg")
# print(os.listdir())
# import csv
# import csv
# with open('test.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"])
# with open('test.csv', 'r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# divide_numbers = 7 / 0
# print(divide_numbers)
# print(dir(locals()['__builtins__']))
#Exception Handling in Python
# try:
#     divide_numbers = 7 / 0
#     print(divide_numbers)
# except:
#      print("The number is not divisible by 0")

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass

## you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
        
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

## Python Objects
## create class
# class Bike:
#     name = ""
#     gear = 0

# # create objects of class
# bike1 = Bike()
# bike2=Bike()
# bike1.name="Classic 350 bullet"
# bike1.gear=5
# bike2.name="Pulser 220F"
# bike2.gear=4
# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
# print(f"Name: {bike2.name}, Gears: {bike2.gear} ")

## Create objects of class using python methods
# class Room:
#     length=1
#     breadth=4
#     def calculate_area(self):
#         print("Area of Room =", self.length * self.breadth)

# # create object of Room class
# study_room = Room()

# # assign values to all the properties 
# study_room.length = 42.5
# study_room.breadth = 30.8

# # access method inside class
# study_room.calculate_area()

# ## Using Constructor
# class Bike:
#     # constructor function    
#     def __init__(self, name = ""):
#         self.name = name
#         print("Hello from the constructor")

# bike1 = Bike("Mountain Bike")
# print(bike1.name)

##Example: Python Inheritance
# class Animal:

#     # attribute and method of the parent class
#     name = ""
    
#     def eat(self):
#         print("I can eat")

# # inherit from Animal
# class Dog(Animal):

#     # new method in subclass
#     def display(self):
#         # access name attribute of superclass using self
#         print("My name is ", self.name)

# # create an object of the subclass
# labrador = Dog()

# # access superclass attribute and method 
# labrador.name = "Rabindra Kumar Sah"
# labrador.eat()

# # call subclass method 
# labrador.display()

# import time

# time.sleep(200)
# print("Wait until 200 seconds.")
# # Output: Wait until 2 seconds.

import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Perform some operations
print("Array:", array)
print("Sum of array:", np.sum(array))
print("Mean of array:", np.mean(array))
print("Square of array:", np.square(array))
print("Standard Deviation:", np.std(array))
matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)
print("Inverse of matrix:\n", inverse)

array = np.array([[1, 2, 3], [4, 5, 6]])
print("Reshaped array:\n", array.reshape(3, 2))
print("Transposed array:\n", array.T)
array1 = np.array([1, 2, 3])
array2 = np.array([[1], [2], [3]])
print("Broadcasted addition:\n", array1 + array2)
from PIL import Image
import numpy as np

# Load an image and convert to NumPy array
image = Image.open("C&C Desktop.png")
image_array = np.array(image)
print("Image shape:", image_array.shape)
print(np.__version__)
