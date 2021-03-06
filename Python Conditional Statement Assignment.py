#!/usr/bin/env python
# coding: utf-8

# - Q.1 Take two integer values from the user and print greatest among them.  

# In[1]:


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(a >= b):
    print(a, "is greater")
else:
    print(b, "is greater")


# - Q.2 Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd. 

# In[2]:


# Case - 1
input_num = int(input('Enter any number: '))
if input_num % 2 == 0:
    print(input_num, "is EVEN")
else:
    print(input_num, "is ODD")


# In[7]:


# Case - 2
input_num = int(input('Enter any number: '))
if input_num % 2 == 0:
    print(input_num, "is EVEN")
else:
    print(input_num, "is ODD")


# - Q.3. Create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program        should display a message indicating that the entered letter is a vowel. If the user enters y then your program should          display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should        display a message indicating that the letter is a consonant. 

# In[6]:


# Case - 1
ch = input("Input a letter of the alphabet: ")

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("ch is a vowel.")
elif ch == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for y consonant.")
else:
    print("ch is a consonant.") 


# In[8]:


# Case -2
ch = input("Input a letter of the alphabet: ")

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("ch is a vowel.")
elif ch == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for y consonant.")
else:
    print("ch is a consonant.") 


# In[9]:


# Case -3
ch = input("Input a letter of the alphabet: ")

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("ch is a vowel.")
elif ch == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for y consonant.")
else:
    print("ch is a consonant.") 


# - Q.4 A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene. Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle’s type.

# In[10]:


# Case - 1
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")


# In[11]:


# Case - 2
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")


# In[12]:


# Case - 3
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")


# - Q.5 Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and       then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3       up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an       appropriate error message. 

# In[15]:


# Case - 1
a=int(input())
if (a == 3):
    print("Triangle")
elif (a == 4):
    print("Quadrilateral")
elif (a == 5):
    print("Pentagon")
elif( a == 6):
    print("Hexagon")
elif( a == 7):
    print("Heptagon")
elif( a == 8):
    print("Octagon")
elif( a == 9):
    print("Nonagon")
elif( a == 10):
    print("Decagon")
    
else:
          print ("Error, sides must be in between 3 and 10. Please try again.")


# In[16]:


# Case - 2
a=int(input())
if (a == 3):
    print("Triangle")
elif (a == 4):
    print("Quadrilateral")
elif (a == 5):
    print("Pentagon")
elif( a == 6):
    print("Hexagon")
elif( a == 7):
    print("Heptagon")
elif( a == 8):
    print("Octagon")
elif( a == 9):
    print("Nonagon")
elif( a == 10):
    print("Decagon")
    
else:
          print ("Error, sides must be in between 3 and 10. Please try again.")


# - Q.6 A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity,             suppose, one unit will cost 100. Judge and print total cost for user. 

# In[7]:


price=int(input("enter price: "))
qty=int(input("enter quantity: "))
cost=price*qty
if cost>1000:
    print ("10% discount applicable")
    discount=cost*10/100
    cost=cost-discount
print ("Total payable cost for user is :", cost)


# - Q.7 Take input of age of 3 people by user and determine oldest and youngest among them. 

# In[10]:


person1 = eval(input("Enter age of person 1 : "))
person2 = eval(input("Enter age of person 2 : "))
person3 = eval(input("Enter age of person 3 : "))

# check oldest
if person1 > person2 and person1 > person3:
    print("Person 1 is oldest")
elif person2 > person1 and person2 > person3:
    print("Person 2 is oldest")
elif person3 > person1 and person3 > person2:
    print("Person 3 is oldest")

# check youngest
if person1 < person2 and person1 < person3:
    print("Person 1 is youngest")
elif person2 < person1 and person2 < person3:
    print("Person 2 is youngest")
elif person3 < person1 and person3 < person2:
    print("Person 3 is youngest")


# - Q.8 A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years. Ask user for           their salary and year of service and print the net bonus amount. 

# In[11]:


salary = eval(input("Enter your salary:"))
service_yrs = eval(input("Enter Years of service:"))
if service_yrs > 5:
    print("Yours salary(+Bonus) = ",salary + (salary)*5/100)
else:
     print("You are not eligible for bonus as you have less service years.")


# - Q.9 Write a program to check if a year is leap year or not. If a year is divisible by 4 then it is leap year but if the year           is a century year like 2000, 1900, 2100 then it must be divisible by 400. 

# In[16]:


# User enters the year
year = int(input("Enter Year: "))
# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# - Q.10 Accept d1 and d2 as input. First, check to see that they are in the proper range for dice. If not, print a message.            Otherwise, determine the outcome if this is the come out roll. If the sum is 7 or 11, print the winner. If the sum is 2,        3 or 12, print loser. Otherwise print the point.

# In[24]:


import random
def play_one_round(bet):
    # Returns the value of a simulated roll of two dice
     def roll_dice():
        input("Press ENTER to roll the dice...")
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1 + d2
roll = roll_dice()

    # First phase: 7 or 11 wins, 2, 3, or 12 loses
if roll == 7 or roll == 11:
         print("You win!")
        #return bet
elif roll == 2 or roll == 3 or roll == 12:
         print ("Sorry, you lose!")
        #return -bet
else:
        point = roll
        print()
        print ("The point is now", point, ".")
play_one_round(100000000000)


# - Q.11 . Write a python program to display the number of days in a month name from the given list of months or month number              entered by user. 

# In[1]:


# Case - 1
month = int(input())
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Number of days is 31")
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):
     print("Number of days is 29")
elif(month == 2):
    print("Number of days is 28")
else:
    print("Number of days is 30")


# In[4]:


# Case - 2
month = int(input())
year = int(input())
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Number of days is 31")
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):
     print("Number of days is 29")
elif(month == 2):
    print("Number of days is 28")
else:
    print("Number of days is 30")


# In[5]:


# Case - 3
month = int(input())
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Number of days is 31")
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):
     print("Number of days is 29")
elif(month == 2):
    print("Number of days is 28")
else:
    print("Number of days is 30")


# - Q.12 Write a Python program to get next day of a given date.

# In[6]:


year = int(input("Input a year: "))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
    
month = int(input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


# In[ ]:





# In[ ]:




