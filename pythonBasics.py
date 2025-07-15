# ------------------------------------------------------------------------------

name = input("Enter Your Name: ")  # input statement
# the type of the input always str.
# so  if we want it to be another type we use casting:
# str(the_variable), float(the_variable), bool(the_variable), str(the_variable).
# For Example:
age = int(input("Enter Your Age: "))

# ------------------------------------------------------------------------------

print("Hello", name)  # output statement
# THE OUTPUT: Hello Jana
# there is a spce because ( , = space).
# in print statement we can use + to print +2 variable together
# NOTE: to use +, the variable must be str, so we will use casting.
# For Example:
# print("Hello " + name + "\nYour age is" + age ) -> ERROR
print("Hello " + name + "\nYour age is" + str(age))
# or we can write:
print("Hello", name, "\nYour age is", age)

# ------------------------------------------------------------------------------

# variable type: int, float, bool, str.
# To know the type we will use type(the_variable) method.

# ------------------------------------------------------------------------------

# import math
# math.ceil() -> math.ceil(3.14) -> 4 -> the smallest int num greater than 3.14
# math.floor() -> math.floor(3.14) -> 3 -> the greatest int num smaller than 3.14
# math.sqrt() -> math.sqrt(9) -> 3
# round() -> round(3.14) -> 3
# abs() -> abs(-3.14) -> 3.14
# pow( , ) -> pow(3.14,2 ) -> 9.8596
# max( , ) or max( , , ) -> max(a,b) -> b, if a=1 and b=2
# min( , ) or min( , , ) -> max(a,b) -> a, if a=1 and b=2

# ------------------------------------------------------------------------------

# x**y -> y is the power of x -> ex: 4**2 = 4^2 = 16
# x//y -> (Floor Division) without floating points (.00) -> 5//2 = 2

# ------------------------------------------------------------------------------

# if, elif, else:

n = 4
if n*6 > n**2 or n%2 == 0: # => True or True => True
    print("Check") # Output: Check

number = -4
if number > 0:
 print('Number is positive.')
elif number == 0:
 print('Number is zero.')
else:
 print('Number is negative.')

 print(10 > 1)
 # True
 print("cat" == "dog")
 # False
 print(1 != 2)
 # True
 print(1 < "1")
 # Will return a type error
 print(1 == "1")
 # False
 print(not 42 == "Answer")
 # True

 # To compare two string -> COMPARE THE FIRST CHAR ONLY FOR EACH WORD

 print("Wednesday" > "Friday")
 # True
 # The greater than > operator checks if the left string has a higher
 # Unicode value than the right string. If true, the Python interpreter
 # returns a True result. Since W has a Unicode value of 87, and you can
 # easily calculate that F has a Unicode value of 70, this comparison is
 # the same as 87 > 70. As this is true, Python will return a True
 # result.
 print("Five" < 6)
 # False
 # greater than > and less than operators < cannot be used to compare
 # two different data types.

 def hint_username(username):
     if len(username) < 3:
         print("Invalid username. Must be at least 3 characters long")

 # ------------------------------------------------------------------------------

def calc(x):
 '''function for calc'''
 #هذي الثلاث شرطات تستعمل عشان توثيق الدالة بحيث لو الشخص حط اسم الدالة داخل help() يطلع له ذا النص
 return x - 75

calc(75)
help(calc)

# ------------------------------------------------------------------------------

# print(7+"8") -> this will throw an error

# ------------------------------------------------------------------------------

round(30.155, 2)
# للتقريب إلى منزلتين

# ------------------------------------------------------------------------------

time_list = [12, 2, 32, 19, 57, 22, 14]

print(sorted(time_list))
# sorted() for sorting but not change the original array
print(time_list)

# Output:
# [2, 12, 14, 19, 22, 32, 57]
# [12, 2, 32, 19, 57, 22, 14]

print(min(time_list))
print(max(time_list))

# Output:
# 2
# 57

# ------------------------------------------------------------------------------

print(len("key"))
# len() -> the length of the string

# ------------------------------------------------------------------------------

# LOGIC -> and, or, not

# ------------------------------------------------------------------------------

# LOOPS

# 1. while loop
# while loop is used to execute a block of code repeatedly as long as a given condition is true
#1
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))
#2
while my_variable < 10:
    print("Hello")
    my_variable += 1
#This code will give a NameError
#Variable is not defined 
while x != 0 and x % 2 == 0:
    x = x / 2
#No output 
 
# 2. for loop
# for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# for i in range(x, y, z): # x = start, y = stop, z = step
# 1 stop
for i in range(5): 
 print("This is fun!") # Spece = {} = Block
 
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends: # friend = i
    print("Hi " + friend)
# -----------------------------------------------------
 # 2 start, stop
for i in range(1, 6):
    print(i) # Output: 1, 2, 3, 4, 5
# -----------------------------------------------------
# 3 start, stop, step
for i in range(1, 10, 2): 
    print(i) # Output: 1, 3, 5, 7, 9
for i in range(10, 0, -1):  
    print(i) # Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# -----------------------------------------------------

# ------------------------------------------------------------------------------
