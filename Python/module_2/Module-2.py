# Write a Python program to check if a number is positive, negative or zero.

a = int(input("Enter a number : "))
if a < 0:
    print("Number is negative")
elif a > 0:
    print("Number is positive")
else:
    print("Number is Zero")


# Write a Python program to get the Factorial number of given number.

a = int(input("Enter a number to find factorial: "))
factorial = 1

for a in range(a, 0, -1):
    factorial = factorial * a

print(f"{factorial}")

# Write a Python program to get the Fibonacci series of given range.
Series_num = int(
    input("Enter the quantity of numbers you want in the fibonacci series :- "))
fibonacci = []
start_num = 1

for Series_num in range(0, Series_num-1, 1):
    if fibonacci == []:
        fibonacci.append(1)
        fibonacci.append(1)
    last_two_sum = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(last_two_sum)

print(fibonacci)


# How memory is managed in Python?

# Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.

# What is the purpose continue statement in python?

# The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.


# Write python program that swap two number with temp variable and without temp variable.
a = int(input("Enter Number A : "))
b = int(input("Enter Number B : "))
c = a
a = b
b = c
print("Number A is ", a)
print("Number B is ", b)


x = int(input("Enter Number X : "))
y = int(input("Enter Number Y : "))
x = x + y
y = x - y
x = x - y
print("Number X is ", x)
print("Number Y is ", y)


# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

num = int(input("Enter a Number : "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Write a Python program to test whether a passed letter is a vowel or not.

letter = int(input("Enter a letter : "))

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter is a vowel")
else:
    print("The letter is not a vowel")

# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
sum = 0
if a == b or b == c or c == a:
    print("The sum of three numbers is 0")
else:
    sum = a+b+c
    print("The sum of three numbers is ", sum)

# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
status = True
if a == b or a+b == 5 or a-b == 5 or b-a == 5:
    status = True
else:
    status = False
print(status)

# Write a python program to sum of the first n positive integers.

n = int(input("Enter a number : "))
sum = 0
for n in range(0, n+1, 1):
    sum = sum + n
print(f"{sum}")

# Write a Python program to calculate the length of a string.

str = input("Enter a string : ")
print("The length of string is ", len(str))

# Write a Python program to count the number of characters (character frequency) in a string

mystr = input("Enter a string : ")
mystr.count('p')
print("P: ", mystr.count('P'))


# What are negative indexes and why are they used?
# Negative Indexing is used to in Python to begin slicing from the end of the string
# eg. if "Herit" is a string, the -1 index would give the value 't'


# Write a Python program to count occurrences of a substring in a string.
myStr = 'The sun is a huge ball of gases. It has a diameter of 1,392,000 km. It is so huge that it can hold millions of planets inside it. The Sun is mainly made up of hydrogen and helium gas. The surface of the Sun is known as the photosphere.'
print(myStr.count('is'))

# Write a Python program to count the occurrences of each word in a given sentence
myStr = input("Enter a string : ")
list = []
list = myStr.split()
for p in list:
    frequency = [list.count(p)]
print(dict(zip(list, frequency)))


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
x = str1[0:2]
str1 = str1.replace(str1[0:2], str2[0:2])
str2 = str2.replace(str2[0:2], x)
print(str1, str2)

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
string = input("Enter a string : ")
if len(string) >= 3:
    if string.endswith("ing"):
        string = string.replace('ing', 'ly')
    else:
        string = string + "ing"
else:
    string = string
print(string)


# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
string = input("Enter a string : ")
stringList = string.split()
if stringList.index('not') > stringList.index('poor'):
    string = string.replace('not', 'good')
    string = string.replace('poor', 'good')
else:
    string = string
print(string)

# Write a Python function that takes a list of words and returns the length of the longest one.
myList = []
length = 0
largestWord = ''
num = int(input('How many words do you want to add in the list? : '))
for items in range(num):
    element = input(f'Enter List element {items+1}: ')
    myList.append(element)
for word in myList:
    if len(word) > length:
        length = len(word)
        largestWord = word
    else:
        length = length
print(f"The largest word is {largestWord} and the length is {length}")

# Write a Python function to reverses a string if its length is a multiple of 4.
enterString = input("Enter a string : ")
if len(enterString) % 4 == 0:
    enterString = enterString[::-1]
else:
    enterString = enterString
print(enterString)

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
enterString = input("Enter a string : ")
firstTwo = enterString[0:2]
lastTwo = enterString[-2:]
if len(enterString) < 2:
    print(enterString)
else:
    enterString = firstTwo + lastTwo
    print(enterString)

# Write a Python function to insert a string in the middle of a string.
str = "My is Herit"
word = "Name"
str = str[:3] + word + str[2:]
print(str)
