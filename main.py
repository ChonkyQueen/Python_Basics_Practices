# Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.

print((15 + 30) / 2)

# Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.

a = 15
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Create a variable called name and store your name in it as a string.

name = "Jeff"

# Create three variables in one line and assign each one a different food item.

a, b, c = "apple", "banana", "orange"

# Print out "Hello" ten times using arithmetic operators.

print("Hello" * 10)

# Set your name and age variables in one line with multiple assignment

name, age = "Jeff", 16

# Create two strings and then create a third variable combining both of the two original strings.

x = "Hi!"
y = "LOL!"
sentence = x + " " + y

# Create a string and print the fourth letter of the word.

x = "I love you!"
print(x[4])

# Create a string and print the letters from index 0 to 5.

sent1 = "That's an adorable dog!"
print(sent1[0:5])

# Create a variable and print all the letters from the first index until the end.

sent2 = "The other day, I saw a dog dancing around!"
print(sent2[0:])

# Lists!

shopping_list = ['apples', 'oranges', 'bananas', 'milk', 'carrots']
print(shopping_list[0])
print(shopping_list[2])
print(shopping_list[0:3])

# Adding items to the list
shopping_list.append('muffins')
print(shopping_list)
shopping_list[0] = 'cherries'
print(shopping_list)
del shopping_list[3]
print(shopping_list)

# length of list
print(len(shopping_list))

shopping_list_2 = ["bread", "jam", "butter"]
print(shopping_list + shopping_list_2)

# max and min

list_num = [1, 5, 2, 6, 10]
print(max(list_num))
print(min(list_num))

# Dictionaries

students = {"bob": 12, "rachel": 15, "emily": 20}
students["rachel"] = 16
del students["emily"]
print(students)
# keep each key to unique to prevent confusion for Python!

# Tuples
# Tuples are immutable - they can't be modified

tup = ("oranges", "apples", "bananas")
print(tup)
# tup[0] = "cherries" will give an error
tup2 = (12, 14)
tup3 = tup + tup2
print(tup3)

# Excercise 2

# 1. Create a list of names and print the second item.

names = ["jerry", "stuart", "jeff", "amanda"]
print(names[1])

# 2. Create a list of sports and then replace the second item with another sport.

sports = ["basketball", "football", "badminton", "table tennis", "volleyball"]
sports[0] = "rugby"
print(sports)

# 3. Create a list containing numbers and delete the fifth number from the array.

numbers = [1, 15, 45, 7634, 23]
del numbers[4]
print(numbers)

# 4. Create two lists of numbers and merge them.

num_list_1 = [15, 42, 56, 68]
num_list_2 = [45, 54, 62, 65]
print(num_list_1 + num_list_2)

# 5. Create a list of numbers and find the length, minimum, and maximum.

numbers = [14, 56, 52, 78, 74, 35]
print(len(numbers))
print(min(numbers))
print(max(numbers))

# 6. Create a dictionary of students and scores and print out a student’s score.

student_scores = {"bob": 30, "jerry": 2, "bill": 69, "amanda": 22}
print(student_scores["bob"])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.

students_ages = {"bob": 16, "amanda": 15, "bill": 23, "sally": 24}
del students_ages["amanda"]
print(students_ages)

# 8. Create a dictionary of names and ages and then print out all the keys and values

names_and_ages = {"jimmy": 18, "donald": 25, "john": 28, "rachel": 29}
print(names_and_ages)

# 9. Create a tuple of your favorite movies

tup4 = ("Frozen", "Puss In Boots", "Shrek 2", "The Three Idiots")
print(tup4)

# 10. Create a tuple and print all the items from the first to third index.

tup5 = ("milk", "orangutan", "bird", "penguin")
print(tup5[0:3])

# Conditional Statements

if 5 > 3:
    print("hello")
else:
    print("condition was not true")

# relational operators
# > < >= <= == !=

if 5 == 2:
    print("hi!")

# else if statements
age = 16
if age <= 13:
    print("You are a child")
elif age >= 13 and age <= 18:
    print("You are a teenager")
else:
    print("You are an adult")

# logical operators
# and / or

# Introduction to For Loops

list6 = ["apples", "bananas", "cherries"]
tup6 = (2, 6, 10)

for item in list6:
    print(item)
for item in tup6:
    print(item)

for x in range(0, 21, 5):
    print(x)

for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)

# Introduction to While Loops
# 3 control statements - break, continue, pass

c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass
    print(c)

# Try and Except statements
# Useful in situations when exceptions may be raised
try:
    if name > 3:
        print("hello")
except:
    print("An error was detected.")


# Welcome to Functions!

# A baker makes Avi's special bread
# Series of steps: mix, knead, rise, bake

# make_special_bread() performs these steps

def hello_world():
    print("Hello World!")


hello_world()


def greeting(name):
    print("Hi " + name + "!")


greeting("Avi")


def addition(num1, num2):
    print(num1 + num2)


addition(4, 5)


def addition(num1, num2):
    return num1 + num2


num_sum = addition(12, 34)
print(num_sum)


def mul(num1, num2):
    return num1 * num2


print(mul(addition(1, 2), addition(3, 4)))

# Built-in Python Functions

# absoulte value
print(abs(-5))

# bool
print(bool(None))

# dir
print(dir("Hello"))

# help
# print(help("Hello".upper))

# eval
sent = "print('hi')"
eval(sent)

# exec - eval, but multiple lines

# str, int, float
print("hello" + str(100))
print(123 + int("456"))
print(float("123.45") + 0.23)


# Object Oriented Programming - Classes and Objects

# Class: Dog
# Properties: name, age, breed...
# Methods: bark, eat, sleep...

# Object 1, 2, 3...
# Properties: fido, 5, german shepherd...

# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


p1 = Person("Bob", 22)
print(p1.getAge())


# OOP - Class Inheritance

# Base model - engine, wheels, etc.
# Sports model - powerful engine...

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5

    def drive(self):
        print("Driving a car...")


class SportsCar(Car):
    def __init__(self):
        # Remember this executes the init function of the parent class
        super().__init__()
        self.engine_power = "400 HP"
        self.seats = 2


def drive(self):
    print("Driving a sports car...")


mySportsCar = SportsCar()
mySportsCar.drive()