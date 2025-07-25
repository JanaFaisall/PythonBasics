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

# Spece Before = {} = Block

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
 print("This is fun!")
 
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
# 4. nested loop
# A nested loop is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop.
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ") # end=" " is used to print in the same line
  print()
# Output:
# [0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6]
# [1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
# [2|2] [2|3] [2|4] [2|5] [2|6]
# [3|3] [3|4] [3|5] [3|6]
# [4|4] [4|5] [4|6]
# [5|5] [5|6]
# [6|6]

# 5
greeting = 'Hello'

for letter in greeting:
 print("The next character is: ", letter)
 # Output: The next character is:  H
 # The next character is:  e
 # The next character is:  l
 # The next character is:  l
 # The next character is:  o

for i in range(len(greeting)):
 print(i) 
# Output: 0
 # 1
 # 2
 # 3
 # 4

i = 0
while i < len(greeting):
	print(greeting[i]) # indexing
    # This will print one character at a time
	i += 1
# Output: H
# e
# l
# l
# o

greeting = 'Hello'
i = 0
while i < len(greeting):
 print(greeting[i:i+2]) # slicing
 # This will print two characters at a time
 i += 1
 # Output: He
 # el
 # lo

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

num1 = 0 
num2 = 0

for x in range(5):
    num1 = x #4
    for y in range(14):
        num2 = y + 3 # 13 +3 = 16

print(num1 + num2) #4 + 16 = 20


# ------------------------------------------------------------------------------
#Strings
# String - Concatenation (الربط)
greeting = "Hello"
name = "Jana"
print(greeting + " " + name)  # Hello Jana

# String - Repetition (التكرار)
print(greeting * 3)  # HelloHelloHello

# String - Length (الطول)
print(len(greeting))  # 5 (عدد الحروف في النص)

# String - Case Conversion (تحويل الحالة)
print(greeting.lower()) # hello
print(greeting.upper())  # HELLO

# String - Finding Substrings (البحث عن أجزاء من النص)
text = "Hello, welcome to Python programming!"
print(text.find("welcome"))  # 7 (موقع الكلمة "welcome" في النص)
print(text.find("Python"))  # 15 (موقع الكلمة "Python" في النص)
print(text.find("Java"))  # -1 (لا توجد الكلمة "Java" في النص)

# String - Replacing Substrings (استبدال أجزاء من النص)
print(text.replace("Python", "Java"))  # Hello, welcome to Java programming!

# String - Splitting and Joining (التقسيم والانضمام)
sentence = "Python is fun"
words = sentence.split()    # ['Python', 'is', 'fun'] (تقسيم الجملة إلى كلمات)
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))  # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
print("-".join(test.split()))  # How-much-wood-would-a-woodchuck-chuck (انضمام الكلمات إلى جملة)

print("-".join(test.split())) # How-much-wood-would-a-woodchuck-chuck (انضمام الكلمات إلى جملة)
print(" ".join(words))  # Python is fun (انضمام الكلمات إلى جملة)
" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]) # This is a phrase joined by spaces

# String - Checking Prefix and Suffix (التحقق من البادئة واللاحقة)
filename = "example.txt"
print(filename.startswith("example"))  # True (الملف يبدأ بـ "example")
print(filename.endswith(".txt"))  # True (الملف ينتهي بـ ".txt")

# String - Checking Membership (التحقق من العضوية)
text = "Hello, World!"
print("Hello" in text)  # True (الكلمة "Hello" موجودة في النص)
print("Python" in text)  # False (الكلمة "Python" غير موجودة في النص)

# String - Formatting (التنسيق)
name = "Jana"
age = 25
print(f"My name is {name} and I am {age} years old.")  # My name is Jana and I am 25 years old.

# String - Checking if String is Alphanumeric (التحقق مما إذا كان النص أبجدي رقمي)      
text = "Hello123"
print(text.isalnum())  # True (النص يحتوي على أحرف وأرقام فقط)
text = "Hello 123"
print(text.isalnum())  # False (النص يحتوي على مسافات)

# String - Checking if String is Alphabetic (التحقق مما إذا كان النص أبجدي)
text = "Hello"
print(text.isalpha())  # True (النص يحتوي على أحرف فقط)
text = "Hello123"   
print(text.isalpha())  # False (النص يحتوي على أرقام)

# String - Checking if String is Numeric (التحقق مما إذا كان النص رقمي)
text = "12345"
print(text.isdigit())  # or text.isnumeric() -> True (النص يحتوي على أرقام فقط)
text = "12345abc"
print(text.isdigit())  # False (النص يحتوي على أحرف)

# String - Stripping Whitespace (إزالة الفراغات)
text = "   Hello, World!   "
print(text.strip())  # Hello, World! (إزالة الفراغات من البداية والنهاية)
print(text.lstrip())  # Hello, World!   (إزالة الفراغات من البداية فقط)
print(text.rstrip())  #    Hello, World! (إزالة الفراغات من النهاية فقط)

# String -  Slicing (التقطيع أو القص)
text = "Programming"
print(text[0])      # P   (الحرف الأول)
print(text[-1])     # g   (الحرف الأخير)
print(text[3:7])    # gram (الحروف من 3 إلى 6)
print(text[:6])     # Progra (من البداية حتى 5)
print(text[6:])     # ming (من 6 إلى النهاية)
print(text[::2])    # Pgamn (كل حرف ثاني)
print(text[::-1])   # gnimmargorP (النص مقلوب)

pets="Cats & Dogs"
pets.index("t") # 1
pets.index("x") # ValueError: substring not found
"t" in pets # True
"x" in pets # False

"The number of times e occurs in this string is 4".count("e") # 4

for c in "abcde": print(c) # Output:
# a
# b
# c
# d
# e

# String - Formatting with f-strings (تنسيق النصوص باستخدام f-strings)
# 1 - Using f-strings
name = "Jana"
age = 25
print(f"My name is {name} and I am {age} years old.")  # My name is Jana and I am 25 years old.
# 2 - Using format method
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number)) # Hello Manny, your lucky number is 15.
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3)) # Your lucky number is 15, Manny.

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) # :>3 means right-align the number in a field of width 3
# Output:
#  0 F |  -17.78 C  
# 10 F |  -12.22 C
# 20 F |   -6.67 C
# 30 F |   -1.11 C
# 40 F |    4.44 C
# 50 F |   10.00 C
# 60 F |   15.56 C
# 70 F |   21.11 C
# 80 F |   26.67 C
# 90 F |   32.22 C
#100 F |   37.78 C

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# Output: 7.5 8.18 
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Output: Base price: $7.50. With Tax: $8.18
basket = [
 ("Peaches", 3.0, 2.99),
 ("Pears", 5.0, 1.66),
 ("Plums", 2.5, 3.99)
]

# Dictionary Formatting

my_dict = {
    "name": "Jana",
    "age": 21,
    "major": "Computer Science"
}
print("Name: {name}, Age: {age}, Major: {major}".format(my_dict))
# Output: Name: Jana, Age: 21, Major: Computer Science   

# ------------------------------------------------------------------------------
