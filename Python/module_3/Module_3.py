# What is List? How will you reverse a list?
"""
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data

a built-in function called reverse() is used to reverse the list. This simple and quick way to reverse a list in Python requires little memory. Syntax: list_name. reverse() Here, list_name means you have to write the list's name, which has to be reversed.
"""

# How will you remove last object from a list?Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

l=[2,33,222,14,25]
print(l)
print("remove last element of list:", l.pop())
print(l[-1])



# Differentiate between append () and extend () methods?
"""
append() adds a single element to the end of the list while . extend() can 
add multiple individual elements to the end of the list.
"""

# Write a Python function to get the largest number, smallest num and sum of all from a list.

def numberFunction(l):
    sum = 0
    for i in l:
        sum += i
    largest = max(l)
    smallest = min(l)
    print(f"""
    Largest number is {largest}
    Smallest number is {smallest}
    Sum of list is {sum}
    """)


listNum = [12, 21, 98, 34, 54, 23, 87, 99, 23]
numberFunction(listNum)


# How will you compare two lists?
""" sort() method or the sorted() function with the == operator
    set() function with the == operator
    reduce() and map() functions with the == operator
    collection.Counter() class with the == operator"""


# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

strList = ["Eve", "Alice", "Bob", "Ishani", "Kombucha"]
count = 0
for i in strList:
    if len(i) > 1 and i[0].capitalize() == i[-1].capitalize():
        count = count + 1
print("Total String count :", count)


# Write a Python program to remove duplicates from a list.
strList = ["red", "orange", "yellow", "green", "blue", "orange", "yellow"]
mySet = set(strList)
strList = list(mySet)
print(strList)


# Write a Python program to check a list is empty or not.

strList = ["red", "orange", "yellow", "green", "blue",]
if len(strList) > 0:
    print("The list is not empty")
else:
    print("The list is empty")


# Write a Python function that takes two lists and returns true if they have at least one common member.

def checkList(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                print("True")
                return True
    print("False")
    return False


list1 = [1, 3, 5, 7, 9, 15, 17]
list2 = [2, 4, 6, 8, 10, 11, 12, 14]
checkList(list1, list2)


# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
list1 = []
list2 = []

for i in range(1, 31):
    list1.append(i*i)
for j in range(0, 5):
    list2.append(list1[j])
for k in range(25, 30):
    list2.append(list1[k])

print(list1)
print(list2)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

strList = ["Ahuja", "Ishani", "Ahuja", "I",
              "Kombucha", "Trumpet", "Gondola", "Kombucha"]


def uniqueList(l):
    mySet = set(l)
    l = list(mySet)

    print(l)


uniqueList(strList)

# Write a Python program to convert a list of characters into a string.

list = ['a', 'n', 'u', 'j', 'l', 'i', 'k',
          'e', 's', 'p', 'y', 't', 'h', 'o', 'n']
Str = ""

for i in list:
    Str += i

print(Str.capitalize())

# Write a python program to select an item randomly from a list.

import random
color = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color))


# Write a Python program to find the second smallest number in a list.

list = [2, 4, 6, 8, 10, 11, 12, 14]

smallest = min(list)
list.remove(smallest)

secondSmallest = min(list)
print(secondSmallest)

# Write a Python program to get unique values from a list

mylist = [2, 4, 6, 8, 10, 11, 12, 14, 14, 12, 6]

for i in mylist:
    for j in mylist:
        if i == j:
            mylist.remove(j)
print(mylist)

# Write a Python program to check whether a list contains a sub list

mylist = [2, [4, 6, 8], [10, 12, 14], 16, 18, 20, [22, 24, 26], 28, 30]

for i in mylist:
    if type(i) == list:
        print(f"This is a sublist {i}")
    else:
        print(i)

# Write a Python program to split a list into different variables

list = [2, [4, 6, 8], [10, 12, 14], 16, 18, 20, [22, 24, 26], 28, 30]
var1, var2, var3, var4, var5, var6, var7, var8, var9 = list

print(f"""  {var1}
            {var2}
            {var3}
            {var4} 
            {var5} 
            {var6} 
            {var7} 
            {var8} 
            {var9}  """)


# What is tuple? Difference between list and tuple. 



# Write a Python program to create a tuple with different data types.

myTuple = (1, 'Ahmedabad', 9.5, True, False, 99, 'Baroda')

for i in myTuple:
    print(i)

# Write a Python program to create a tuple with numbers.

myTuple = (1, 2, 9, 89, 21, 99, 76)
print(myTuple)



# Write a Python program to convert a tuple to a string.
myTuple = ("Hello", "My", "Name", "Is", "Anuj", "And",
           "I", "Am", "Enrolled", "In", "Python", "Course")
myString = ''

for i in myTuple:
    myString = myString + " " + i
print(myString)


# Write a Python program to check whether an element exists within a tuple

myTuple = (1, 2, 9, 89, 21, 99, 76)
myelement = 10
check = False

for i in myTuple:
    if i == myelement:
        check = True


if check == True:
    print("Your element exists in tuple")
else:
    print("Your element does not exist in tuple")


# Write a Python program to find the length of a tuple.

myTuple = (1, 2, 9, 89, 21, 99, 76)
print(len(myTuple))


# Write a Python program to convert a list to a tuple.

mylist = [2, [4, 6, 8], [10, 12, 14], 16, 18, 20, [22, 24, 26], 28, 30]
myTuple = tuple(mylist)

print(myTuple)

# Write a Python program to reverse a tuple.

myTuple = (1, 2, 9, 89, 21, 99, 76)
newTuple = myTuple[::-1]

print(newTuple)


# Write a Python program to replace last value of tuples in a list.
mylist = [1, 2, 3, 4, 5, 6, 7, (8, 9, 0)]
for i in mylist:
    if type(i) == tuple:
        mylist.pop()
        mylist.append(8)
        mylist.append(9)
        mylist.append(10)

print(mylist)


# Write a Python program to find the repeated items of a tuple.

myTuple = (1, 2, 76, 9, 15, 78, 89, 15, 78, 21, 99, 21, 76)

count = myTuple.count(15)
print("Number 15 appears in the tuple ", count, " times")


# Write a Python program to remove an empty tuple(s) from a list of tuples.

mylist = [1, 2, (), 3, 4, 5, 6, 7, (8, 9, 0)]
print(mylist)
for i in mylist:
    if type(i) == tuple:
        if i == ():
            mylist.remove(i)
print(mylist)

# Write a Python program to unzip a list of tuples into individual lists.

# Write a Python program to convert a list of tuples into a dictionary.

# How will you create a dictionary using tuples in python?


# Write a Python script to sort (ascending and descending) a dictionary by value.

# Write a Python script to concatenate following dictionaries to create a new one.

# Write a Python script to check if a given key already exists in a dictionary.

# How Do You Traverse Through A Dictionary Object In Python?

# How Do You Check The Presence Of A Key In A Dictionary?

def check_key(dic,key):
    if key in dic.keys():
        print("Key is present in dictionary")
    else:
        print("Key is not present in dictionary")

dic={'a':1,'b':2,'c':3}
check_key(dic,'a')
check_key(dic,'w')

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

# Write a Python program to check multiple keys exists in a dictionary

student = {
  'name': 'Dev',
  'class': 'VI',
  'roll_id': '1'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Dev'})
print(student.keys() >= {'roll_id', 'name'})

# Write a Python script to merge two Python dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# Write a Python program to map two lists into a dictionary

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# Write a Python program to combine two dictionary adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

# Write a Python program to print all unique values in a dictionary.

Data=[{"A":"DELL1"}, {"A": "DELL2"}, {"B": "DELL1"}, {"B": "DELL5"}, {"C":"DELL5"},
{"A":"DELL9"},{"D":"DELL7"}]
uniqueSet=set()

for i in Data:
    for j in i.values():
        if j not in uniqueSet:
            uniqueSet.add(j)
print(uniqueSet)

# Why Do You Use the Zip () Method in Python?
"""
Python zip() method takes iterable or containers and returns a single iterator object, 
having mapped values from all the containers. It is used to map the similar index of 
multiple containers so that they can be used just using a single entity.
"""

# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd

# Write a Python program to find the highest 3 values in a dictionary?

def Findvalues(dictionary):
    
    sortedItems = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    
    highestValues = [value for key, value in sortedItems[:3]]

    return highestValues


# Example dictionary
my_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 40, 'e': 15}

# Find the highest three values
highestValues = Findvalues(my_dict)

print("The highest three values in the dictionary are:" ,highestValues)



#Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}] Expected Output: Counter ({'item1': 1150, 'item2': 300}) 

# Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the string.      Sample string: 'w3resource' Expected output:{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(x):
    s=1
    while(x!=1):
        s=s*x
        x-=1
    return s

a=int(input("Enter the number : "))
if(a<0):
    print("Please enter possitive numbers !!")
else:
    print(factorial(a))

# Write a Python function to check whether a number is in a given range

def my_range(x):
    if x in range(1,15):
        print(f"{x} is in our range.")
    else:
        print(f"{x} is not in our range.")

my_range(5)
my_range(20)

# Write a Python function to check whether a number is perfect or not.

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
print(perfect_number(16))

# Write a Python function that checks whether a passed string is palindrome or not

a=input("Enter The String : ")
r=a[::-1]

if (a==r):
    print("The string is palindrome")
else:
    print("The string is not palindrome")    

# How Many Basic Types Of Functions Are Available In Python?

"""
There are two types of functions: 
User-defined functions 
    These functions are defined by the user to perform a specific task. 
Built-in functions 
    These functions are pre-defined functions in Python.
"""
# How can you pick a random item from a list or tuple?

"""
In Python, you can randomly sample elements from a list with choice() , sample() , and choices() of the random module. These functions can also be applied to a string and tuple. 
choice() returns one random element, and sample() and choices() return a list of multiple random elements.

"""

# How can you pick a random item from a range?
"""
Use a random.randrange() function to get a random integer number from the given exclusive 
range by specifying the increment. For example, random.randrange(0, 10, 2) will return any 
random number between 0 and 20 (like 0, 2, 4, 6, 8).

"""

# How can you get a random number in python?

"""
To generate random number in Python, randint() function is used. This function is defined in random module.

"""
# How will you set the starting value in generating random numbers?

"""
The seed() method is used to initialize the random number generator. 
The random number generator needs a number to start with (a seed value), to be able to generate a random number. 
By default the random number generator uses the current system time.
"""
# How will you randomizes the items of a list in place? 

"""
The shuffle() method randomizes the items of a list in place.
"""
# Write a Python program to read a random line from a file.
import random

def random_line(fname):
    f=open(fname).read().splitlines()
    print(random.choice(f))

random_line("File.txt")


# Write a Python program to convert degree to radian?

pi=22/7
degree = float(input("Enter degree value: "))
radian = degree*(pi/180)
print(radian)

# Write a Python program to calculate the area of a trapezoid

height = float(input("Height of trapezoid: "))
base_1 = float(input('Base 1 value: '))
base_2 = float(input('Base 2 value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)


# Write a Python program to calculate the area of a parallelogram

base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)

# Write a Python program to calculate surface volume and area of a cylinder

pi=22/7
h=float(input("Enter the height of cylinder : "))
r=float(input("Enter the radius of cylinder : "))
volume = pi*(r**2)*h
surface_area = 2*pi*r*(r+h)
print("Volume : ",volume)
print("Surface Area : ",surface_area)

# Write a Python program to returns sum of all divisors of a number 

a=int(input("Enter the number : "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i

print(f"The sum of all divisiors of {a} : ",sum)

# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers?

from decimal import *

d = list(map(Decimal,'2.5 0.5 00.9 1.5 10.5 12.7 11.9 0.05 20.5'.split()))

print("Max : ", max(d))
print("Min : ", min(d))