"""
# Write a Python program to check whether a list contains a sublist

list = ["Python",11,"tops","technology", 12,10,14,13]
s_list = ["Python","tops", 10,14]
result = []

print(list)
print(s_list)


for i in range(len(s_list)+1): 
    if s_list[i] in list:
        result = s_list[i]     

    else:
        
        print("not a sublist") 

print("yes it contain sublist",reslut)    


# Write a Python program to find the second smallest number in a list.

lst = [21,34,67,11,45,0,87,93]
lst.sort()
print("second smallest number is  :",lst[1])

#lst = [21,34,67,11,45,0,87,93]
#print("second smalllest number is ", sorted(lst)[1])


# Write a Python program to get unique values from a list.

def uniquel(lst):
    return list(set(lst))

my_list = [2,43,1,2,4,6,4,32,45,44,45,4,5,2]
print(uniquel(my_list))



# Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))


# Write a Python program to convert a list of tuples into a dictionary

lst = [("x",1),("y",2),("x",5)]
d= {}
for a,b in lst:
    d.setdefault(a, []).append(b)
print(d)


# Write a Python program to sort a dictionary (ascending /descending) by value.
import operator
d ={2:4,4:6,1:5,5:1,0:0}
print("original dictionary",d)
a_dic = sorted(d.items(), 
             key = operator.itemgetter(1))

s_dic   = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print(a_dic)
print(s_dic)


# Write a Python program to find the highest 3 values in a dictionary

from collections import Counter

dic ={ 'e1': 11, 'e2':56, 'e3':45 , 'e4': 44, 'e5':80, 'e6':78, 'e7':90    }
k = Counter(dic)
max_dic = k.most_common(3)
print("initial dictionary:")
print(dic,"\n")

print("dictionary with highest 3 values: ")
print("keys : values")

for i in max_dic:
    print(i[0]," :",i[1]," ")


# Given a number n, write a python program to make and print the list of Fibonacci series up to n.


def fibo(num):
    if num == 1:
        return 1 
    else:
        a=0 
        b=1
        print(a)
        print(b)
        for i in range(num):
            c = a+b
            print(c)
            a=b
            b=c
        
n= int(input("enter the no : "))
(fibo(n))


# What is List? How will you reverse a list?
# list is a collection of data type. which is used to store multiple data elements in to a single variable.
# it is sperated by commas and enclose by a square brackets. it is mutable,ordered and indexable.
# A built-in function called reverse() is used to reverse the list. 




# How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
#l = [1,3,4,5,6,7,8,9,10]
#l.pop(-1)
#print(l)



# Differentiate between append () and extend () methods? 
# append() method adds a single element to the end of the list, while extend() method adds multiple elements to the end of the list.
# append() method modifies the original list by adding the new element as a single item, while extend() method modifies the original list by adding each element of the iterable as individual items to the end of the list.
l1= [1, 2, 3]
l2 = [4, 5, 6]
l1.append(l2)
print(l1)  
l1.extend(l2)
print(l1)  
    



# Write a Python function to get the largest number, smallest num and sum of all from a list.
def operation_fuc(lst):
    max_num = max(lst)
    min_num = min(lst)
    total = sum(lst)
    return max_num,min_num,total

lst  = [11,45,33,78,45,67,78,98]
max_n,min_n,sum = operation_fuc(lst)
print("maximum no : ",max_n)
print("manimum no : ",min_n)
print("sum of all no : ",sum)



# How will you compare two lists?
by == operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
print("Matched") 





# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

def count_fun(lst):
    c = 0
    for i in lst:
        if len(lst)>=2 and i[0] == i[-1]:
            c = c+1
    return c

lst = ['python', 'programming', 'hello', 'madam', 'world', 'list']
print(count_fun(lst))



# Write a Python program to remove duplicates from a list.
def remove_duplicate(lst):
    return list(set(lst))
lst = [1,3,2,4,1,2,4,6,7,9,9]
print(remove_duplicate(lst))



# Write a Python program to check a list is empty or not.
def empty_check_fun(lst):
    if not lst:
        return True
    else:
        return False
lst1 = []
lst2 = [1,11,111]
print("is empty list : ",empty_check_fun(lst1))
print("is empty list : ",empty_check_fun(lst2))




# Write a Python function that takes two lists and returns true if they have at least one common member.
def myfun(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False
l1 = [1,2,3,56,78,90,12]
l2 = [43,67,54,32,78,22]
l3 = [87,99,87,65,45,67]
print(myfun(l1,l2))
print(myfun(l1,l3))




# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
def square_fun():
    s_lst = [x**2 for x in range(1,31)]
    f_five = s_lst[:5]
    l_five = s_lst[-5:]
    result_list = f_five + l_five
    return result_list
print(square_fun())



## Write a Python program to convert a list of characters into a string.
def covert_fun(lst):
    new_lst = ''.join(lst)
    return new_lst
lst = ['e','k','t','a',' ','m','o','l','i','y','a']
print(lst)
print(covert_fun(lst))




#  Write a Python program to select an item randomly from a list. 
import random
lst = [11,1,34,56,78,90,32,34,45,6,7,9,2,7]
print(random.choice(lst))




# Write a Python program to find the second smallest number in a list.
def myfun(lst):
    lst.sort()
    print("second smallest no : ",lst[1])
lst = [11,1,34,56,78,90,32,34,-1,45,6,7,9,2,7]
print(lst)
myfun(lst)




#  Write a Python program to check whether a list contains a sub list
def contain_sublist(lst,sub_lst):
    if sub_lst in lst:
        return True
    else:
        return False
lst1 = [1,2,3,4,[5,6,7],8,9,10]
s_lst = [5,6,7]
print(contain_sublist(lst1,s_lst))





# Write a Python program to split a list into different variables

my_list = [1, 2, 3, 4, 5]
a, b, c, d, e = my_list
print(a)  
print(b)  
print(c)  
print(d) 
print(e) 




#  What is tuple? Difference between list and tuple.
# tuple is a collection of data type which is immutable means once it is created, you can not modify its elements.
# it is sepearated by commas, and enclosed by parantheses ()
#Lists are defined using square brackets [], while tuples are defined using parentheses ().
# Example of a list
# my_list = [1, 2, 3, 4, 5]
# Example of a tuple
# my_tuple = (1, 'two', 3.0, [4, 5])




#Write a Python program to create a tuple with different data types.
#tuple = ('hello', 42, True, [1, 2, 3], {'a': 1, 'b': 2})
#print(tuple)


#  Write a Python program to create a tuple with numbers
# tuple = (1, 2, 3, 4, 5)
# print(tuple)



#  Write a Python program to convert a tuple to a string.
# tuple = ('h', 'e', 'l', 'l', 'o')
# string = ''.join(tuple)
# print(string)




# Write a Python program to check whether an element exists within a tuple. 
# tuple = ('apple', 'banana', 'cherry', 'orange')
# if 'banana' in tuple:
#     print('banana exists in the tuple')
# else:
#     print('banana does not exist in the tuple')



#  Write a Python program to convert a list to a tuple.
# list = ['apple', 'banana', 'cherry', 'orange']
# tuple = tuple(list)
# print('The tuple converted from the list is:',tuple)



# Write a Python program to reverse a tuple.
# tuple = (1, 2, 3, 4, 5)
# reversed_tuple = tuple[::-1]
# print( reversed_tuple)

#using reversed() method:
def rev_tuple(t):
    t_new = ()
    for i in reversed(t):
        t_new = t_new + (i,)
    print(t_new)
t1= ('e','k','t','a')
rev_tuple(t1)



#  Write a Python program to replace last value of tuples in a list. 

original = [(1,2,3),(2,5,7),(6,3,4)]
new_lst = []
for i in original:
    new_lst.append(i[:-1]+(10,))
print("original list: ",original)
print("new list : ",new_lst)



#  Write a Python program to find the repeated items of a tuple.
tup = (1,2,3,4,5,2,3,4,5,6,7,8,9,3,10,11,12,11,13)
repeated_item = []
for i in tup:
    if tup.count(i)>1 and i not in repeated_item:
        repeated_item.append(i)
print("tuple: ",tup)
print("Repeated item: ",repeated_item)


#  Write a Python program to remove an empty tuple(s) from a list of tuples. 
my_lst = [(),(1,2),(' '),(5),(),(2,5)]
new_lst = [i for i in my_lst if i]
print("orinial list : ",my_lst)
print("new list : ",new_lst)




# Write a Python program to unzip a list of tuples into individual lists.
my_lst = [('a',1),('b',2),('c',3)]
letters, numbers = zip(*my_lst)
print("original list : ",my_lst)
print("letters : ",letters)
print("numbers : ",numbers)



# Write a Python program to convert a list of tuples into a dictionary.
lst = [('a',1),('b',2),('c',3)]
d = dict(lst)
print('original list of tuple : ',lst)
print('dictionary : ',d)



#  How will you create a dictionary using tuples in python? 
# To create a dictionary using tuples in Python, you can pass a list of tuples to the dict() constructor function. Each tuple in the list should contain exactly two elements, where the first element is the key and the second element is the value.
lst = [('a',1),('b',2),('c',3)]
d = dict(lst)
print('original list of tuple : ',lst)
print('dictionary : ',d)



# Write a Python script to sort (ascending and descending) a dictionary by value. 
my_dic = {'a': 7,'b':3,'c':1,'d':5}
ascen = dict(sorted(my_dic.items(), key = lambda x: x[1]))
desc = dict(sorted(my_dic.items(), key = lambda x: x[1], reverse=True))
print("original dictionary : ",my_dic)
print("-----------------------------------------------------------------")
print("sorted dictionary (asending): ",ascen)
print("sorted dictionary (descending): ",desc)

#for i,j in ascen.items():
#   print(f"keys {i} :  {j}")

 
# Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {'a':1, 'b':2}
dic2 = {'c':3, 'd':5}
dic3 = {'e':5, 'f':3}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print("new dictionary : ",new_dic)



#  Write a Python script to check if a given key already exists in a dictionary. 
my_dic = {'apple':30 ,'banana':50,'orange':60}
if 'apple' in my_dic:
    print("key 'apple' already exists in the dictionary.")
else:
    print("key 'apple' doest not exists in the dictionary.")
if 'cherry' in my_dic:
    print("key 'cherry' already exists in the dictionary.")
else:
    print("key 'cherry' does not exists in the dictionary.")



#  How Do You Traverse Through A Dictionary Object In Python? 
# Using a loop.
my_dic = {'apple':3,'banana':5,'cherry':7}
for key in my_dic:
    print(key, my_dic[key])


#  How Do You Check The Presence Of A Key In A Dictionary?
# Using in operator
if 'apple' in my_dic:
    print("key 'apple' already exists in the dictionary.")
else:
    print("key 'apple' doest not exists in the dictionary.")
if 'cherry' in my_dic:
    print("key 'cherry' already exists in the dictionary.")
else:
    print("key 'cherry' does not exists in the dictionary.")



# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
my_dic = {}
for i in range(1,16):
    my_dic[i]= i*i
#print(my_dic)
for i,j in my_dic.items():
    print(i,j)



#  Write a Python program to check multiple keys exists in a dictionary .
#  Using all() function along with a list comprehension to check if multiple keys exist in a dictionary.
def check_keys(dic,key_list):
    return all(i in dic for i in key_list)
my_dic = {'name': 'John', 'age': 25, 'city': 'New York'}
key_to_check = ['name','city','country']
result = check_keys(my_dic,key_to_check)
if result:
    print("all keys exist in the dictionary")
else:
    print("one or more keys  not fount in the dictionary")



# Write a Python script to merge two Python dictionaries 
# To merge two Python dictionaries, update() method or the dictionary unpacking ** operator is used.
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
#dict1.update(dict2)
#print(dict1)

merged_dict = {**dict1,**dict2}
print(merged_dict)


# Write a Python program to map two lists into a dictionary 
empid = ['e11','e12','e13','e14','e15']
empsalary = [40000,42000,50000,55000,80000]
emp_data = dict(zip(empid,empsalary))
print(emp_data)



# Write a Python program to combine two dictionary adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 
# from collections import Counter

from collections import Counter
d1 = {'e1':40,'e2':50,'e3':40}
d2 ={'e1':30,'e2':80,'e3':70}
new_dic = Counter(d1) + Counter(d2)
print(new_dic)




# Write a Python program to print all unique values in a dictionary. 
emp_data = {'e11': 40000,'e12':40000,'e13':50000,'e14':60000,'e15':90000}
unique_value = set()
for i in emp_data.values():
    unique_value.add(i)
print(unique_value)




# Why Do You Use the Zip () Method in Python?
# We use zip() method to simplify the code when we need to iterate over two or more lists at the same time. Instead of using a for loop to iterate over each list separately, we can use zip() to iterate over both lists simultaneously.
# The zip() method can also be used to create a dictionary from two lists, where one list contains keys and the other list contains values.


# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd
import itertools
data = {1:['a','b'], 2:['c','d']}
combination = list(itertools.product(*[data[key] for key in data]))
for i in combination:
    print(''.join(i),end = " ")



#  Write a Python program to find the highest 3 values in a dictionary.
# my_dict = {"a": 10, "b": 5, "c": 20, "d": 15, "e": 30}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# highest_values = [value for key, value in sorted_dict[:3]]
# print("The highest 3 values in the dictionary are:", highest_values)


dic = {'a':6, 'b':8, 'c':2, 'd':5,'e':11, 'f':1, 'g':7, 'h':3}
sort_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
highest_value = [value for key, value in sort_dic[:3]]
print("The highest 3 value in the dictionary are : ", highest_value)
  


### Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] Expected Output:Counter ({'item1': 1150, 'item2': 300}
from collections import Counter
data = [{'item': 'item1','amount': 20}, {'item': 'item2','amount':50}, {'item': 'item3','amount': 80}]
result = Counter()
for i in data:
    result[i['item']] += i['amount']
print(result)




# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. Sample string: 'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
s = "w3school"
dic_count = {}
for i in s:
    if i in dic_count:
        dic_count[i] += 1
    else:
        dic_count[i] = 1
print(dic_count)



# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def fact(n):
    p = 1
    i=1
    while i<=n:
        p=p*i
        i += 1
    return p
print(fact(5))




# Write a Python function to check whether a number is in a given range.
# function
# def check_range(number, range_tuple):
    # return range_tuple[0] <= number <= range_tuple[1]
def test_range(n):
    if n in range(10,20):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(15)




# Write a Python function to check whether a number is perfect or not. 
def is_perfect(num):
     sum_of_divisors = 0
     for i in range(1, num):
         if num % i == 0:
             sum_of_divisors += i
     if sum_of_divisors == num:
         return True
     else:
         return False



# Write a Python function that checks whether a passed string is palindrome or not 
def is_pallindrom(str):
    if str[:]==str[-1::-1]:
        return True
    else:
        return False
print("is string pallindrom :",is_pallindrom("madam "))



# How Many Basic Types Of Functions Are Available In Python? 
# There are two basic types of functions available in Python:
# (1) Built-in functions: These are the functions that are already defined in Python and can be used directly without any need for defining them. Examples include print(), len(), range(), etc.
# (2) User-defined functions: These are the functions that are defined by the user to perform a specific task. They can be called multiple times within a program, and they improve the reusability of the code.


# How can you pick a random item from a list or tuple? 
# To pick a random item from a list or tuple. The random.choice() function can be used to select a random item from a list or tuple.
# import random
# my_list = [1, 2, 3, 4, 5]
# random_item = random.choice(my_list)
# print(random_item)


# How can you pick a random item from a range? 
# The randint() function from the random module. The randint() function takes two arguments: the lower and upper bounds of the range (inclusive), and returns a randomly selected integer from that range.
# import random
# random_number = random.randint(1, 10)  
# print(random_number)


# How can you get a random number in python? 
# By using random module
# import random
# random_number = random.randint(1, 10)  
# print(random_number)


# How will you set the starting value in generating random numbers? 
# By setting the starting value of a random number generator by using the seed() function from the random module. The seed() function takes an integer value as its argument, which will be used as the starting point for the random number generator.


# How will you randomizes the items of a list in place? 
# To randomize the items of a list in place, we can use the shuffle function from the random module.
# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)


# Write a Python program to read a random line from a file. 
import random
filename = "example.txt"
with open(filename, "r") as file:
     lines = file.readlines()
     random_line = random.choice(lines)
     print(random_line)




# Write a Python program to convert degree to radian 
# import math
# def degree_to_radian(degrees):
#     return degrees * math.pi / 180.0
# degrees = 90.0
# radians = degree_to_radian(degrees)
# print(f"{degrees} degrees is equal to {radians:.2f} radians")


# Write a Python program to calculate the area of a trapezoid 
# def area_of_trapezoid(base1, base2, height):
#     area = ((base1 + base2) / 2) * height
#     return area
# base1 = 3
# base2 = 4
# height = 5
# area = area_of_trapezoid(base1, base2, height)
# print("Area of the trapezoid is:", area)


# Write a Python program to calculate the area of a parallelogram 
# base = float(input("Enter the base of the parallelogram: "))
# height = float(input("Enter the height of the parallelogram: "))
# area = base * height
# print("The area of the parallelogram is:", area)


# Write a Python program to calculate surface volume and area of a cylinder 
# import math
# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))
# surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
# volume = math.pi * radius ** 2 * height
# print("The surface area of the cylinder is:", surface_area)
# print("The volume of the cylinder is:", volume)


# Write a Python program to returns sum of all divisors of a number. 
def sum_divisors(num):
    divisors = []
    for i in range(1, num+1):
         if num % i == 0:
             divisors.append(i)
    return sum(divisors)



# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 
decimal_numbers = [3.14, 2.718, 1.618, 0.999, 4.669]
max_number = max(decimal_numbers)
min_number = min(decimal_numbers)
print("The maximum number is:", max_number)
print("The minimum number is:", min_number)



# Mini project : 

# Problem Statement : Password Generator 
# Make a program to generate a strong password using the input given by the user. To generate a password, 
# randomly take some words from the user input and then include numbers, special characters and capital 
# letters to generate the password. Also, keep a check that password length is more than 8 characters. 
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user 
# id, name and password of each user as a tuple.
 
import string
import random

s = []
s1 = string.ascii_letters
s2 = string.ascii_lowercase
s3 = string.ascii_uppercase
s4 = string.punctuation
len = int(input("enter password length\n"))
      
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
print("".join(random.sample(s,len)))

"""

