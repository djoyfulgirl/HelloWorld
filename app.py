import math

# first python program.
print('My name is Tawakalt')

# python program execute line by line from the top.


# datatypes
price = 10  # interger
rating = 4.9  # float
name = 'Tawa'  # spring
is_published = True  # boolean values  Phyton is case sensitive
# print(rating)

# exercise "we check in a patient named john smith. He's 20 years old and is new patient.
# Exercise1
name = 'John Smith'
age = 20
is_new = True
is_existing = True

# name = input( ' What is your name?  ')
# print( 'Hi'  +  name)


# name = input('What is your name? ')
# colour = input('What is your favourite colour? ')
# print( name  +  ' Likes '  +  colour)

# birth_year = input('Birth year: ')
# print(type(birth_year))  # to print the type of variable
# age = 2019 - int(birth_year)    #the built in function int was used
# to allow the sys to understand that the input is a number.
# print(type(age))     # to print the type of variable
# print(age)

# take away

# Exercise 2  Ask a user their weight(in pound), convert it to kilograms and print on the terminal.
# user_weight = input( 'weight : ')
# weight_kilo = float(user_weight) / 2.205
# print(weight_kilo)

# Solution from mosh
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# STRINGS

course = "Python's Course for Beginners"  # You define your string with a double quote to have a single quote in the
# middle of the string.
course = 'Python for "Beginners" '  # To add a double quote in the middle of a string, you will use a single quote.
course = '''    
Hi John,

Here is my our first email to you.

Thank you


'''  # triple quote is use for multiple strings.

# print(course)
# square bracket notation is used to get access to a particular character in a string.
course = 'Python for Beginners'  # to get index of the character  -1 to get the index of the last character.
another = course[:]
# print(another)

# Exercise
name = 'Tawakalt'
# print(name[1:-1])


# formatted string : makes it easier for us to visualise the string.
# formatted string is the one that prefix with a 'f'
first = 'John'
last = 'smith'
message = first + " " + last  # concatenation method
# print(message)
msg = f"{len(first)} {last}"
print(message)

# string methods
# len function is an inbuilt function in python, it can be used to count charcaters
# when a function belongs to something else we refer to it as a method.
# .upper .lower .tittle .find .replace .in

# 14/11/2021

student_name = "Tawakalt"
print(len(student_name))

# escape sequences are \" \' \\ \n
# an expression is a piece of code that produces a value.

# strings methods.
student_name = "Tawakalt"
print(student_name.upper())
print(student_name.count("Tawakalt"))
print(student_name.title())
print(student_name.strip())
print(student_name.find("Ta"))
print(student_name.upper())
print(student_name.rstrip())
print("Taw" in student_name)
print("Das" in student_name)

# numbers methods and arithmetic operators
# x = 20        # this is an integer
# x = 20.5      # this is a float
# x = 2 + 5j    # this is a complex number in coding

print(10 + 2)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 3
x = x + 3
x += 3  # it is an argument assignment operators

# funtions to work with numbers
# print(round(2.9))
# print(abs(-2.9))

print(math.ceil(2.2))    # google python "math module" for other examples of math modules.




