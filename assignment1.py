# # 1. WAP to print the sum of the alternate odd numbers from 1 to 50.

# for i in range(1,50,2):
#     print(i)
#     print(i+2)
#     print("sum of alternate odd numbers from 1 to 50 is",i+(i+2))


# # 2. Create a program that checks if a given year is a leap year. A leap year is either divisible by 4 but not by 100, or it is divisible by 400.

# year=int(input("Enter the year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")   
    
# # 3. Write a program that calculates the cost of admission to a zoo based on age. Admission is free for children under 3, $10 for children aged 3-12, $15 for adults aged 13-59, and $12 for seniors aged 60 and above.    
# age=int(input("Enter the age:"))
# cost=0
# if age<3:
#     cost=0
#     print("Admission is free for children under 3")
# elif age in range(3,13):
#     cost=10
#     print("Admission is $10 for children aged 3-12")
# elif age in range(13,60): 
#     cost=15
#     print("Admission is $15 for adults aged 13-59")
# else:
#     cost=12
#     print("Admission is $12 for seniors aged 60 and above") 
  

# # 4. Create a program that checks if a given year is a century year. A century year is a year that ends with "00". However, it should also be divisible by 400 to be a leap century year.
    
# year=int(input("Enter the year:"))
# if year%100==0 and year%400==0:
#     print(year,"is a leap century year")
# else:
#     print(year,"is not a leap century year")

# # 5. Write a program that categorizes a given temperature into different levels: "Freezing" for temperatures below 0 degrees Celsius, "Cold" for temperatures between 0 and 10 degrees Celsius, "Moderate" for temperatures between 10 and 25 degrees Celsius, and "Hot" for temperatures above 25 degrees Celsius.

# temp=int(input("Enter the temperature in degree celsius:"))
# if temp<0:
#     print("Freezing")
# elif temp in range(0,11):
#     print("Cold")
# elif temp in range(11,26):
#     print("Moderate")
# else:
#     print("Hot")

# # 6. Write a program that asks the user to enter a positive integer and prints a multiplication table for that number up to 20.

# num=int(input("Enter a positive integer:"))
# for i in range(1,21):
#     if num>0:
#         print(num,"*",i,"=",num*i)
#     else:
#         print("Enter a positive integer")
#         break


# # 7. Write a program that takes the user's age as input and categorizes them as a child, teenager, adult, or senior. Additionally, check if the user is eligible to vote (age 18 and above).

# age=int(input("Enter the age:"))    
# if age<12:
#     print("Child")
# elif age in range(13,20):
#     print("Teenager")
# elif age in range(20,60):
#     print("Adult")
# else:
#     print("Senior")

# # 8. Write a program that takes three numbers as input and checks if they form a valid triangle. If valid, determine if it's an equilateral, isosceles, or scalene triangle.

# a=int(input("Enter the first side of the triangle:"))
# b=int(input("Enter the second side of the triangle:"))
# c=int(input("Enter the third side of the triangle:"))
# if a+b>c and b+c>a and c+a>b:
#     if a==b==c:
#         print("Equilateral triangle")
#     elif a==b or b==c or c==a:
#         print("Isosceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Not a valid triangle")

# # 9. Create a program that asks the user for their income and calculates the tax they need to pay based on the following tax brackets: 
# # ● Income up to $10,000: 5% tax
# # ● Income from $10,001 to $50,000: 10% tax
# # ● Income above $50,000: 20% tax

# income=int(input("Enter the income:"))
# if income<=10000:
#     tax=income*0.05
#     print("Tax is",tax)
# elif income in range(10001,50001):
#     tax=income*0.10
#     print("Tax is",tax)
# else:
#     tax=income*0.20
#     print("Tax is",tax)

# # 10. Write a program that checks if a given number is divisible by both 3 and 5, or only by 3 or 5.

# num=int(input("Enter the number:"))
# if num%3==0 and num%5==0:
#     print(num,"is divisible by both 3 and 5")
# elif num%3==0:
#     print(num,"is only divisible by 3")
# elif num%5==0:
#     print(num,"is only divisible by 5")

# Access Modifiers
# 1. Public - Accessible from anywhere
# 2. Private - Accessible only within the class
# 3. Protected - Accessible within the class and its subclasses. can be accessed outside the class but not recommended
# __name - private data member
# _name - protected data member
# name - public data member
# underscore is used to define the access modifiers in python
# protected is shared between the parent and child class.

# Let suppose there is a class Bank account with public data member >> name, acc_type=Saving/Current
# private data member >> acc_bal=0, acc_id
# Method ---> add_details()
#deposit() - add mondey
#withdraw(amount) - deduct money
#get_balance() - return balance
#display() - print all details
# also it should give menu to user to select the options
#1. Withdraw
#2. Deposit
#3. Current Balance
#4. Display

# class Bank:                      # Super class/ Parent class
#     def __init__(self):  #How do we define public and private data members in python
#         self.name=input("Enter the name: ")
#         self.acc_type=input("Enter the account type Savings/Current: ")
#         self.__acc_bal=0
#         self.acc_id=input("Enter the account id: ")
#     def deposit(self):
#         amount=int(input("Enter the amount to deposit: "))
#         self.__acc_bal+=amount
#     def withdraw(self):
#         amount=int(input("Enter the amount to withdraw: "))
#         if amount <= self.__acc_bal:
#             self.__acc_bal-=amount
#         else:
#             print("insuffient balance")
#     def get_balance(self):
#         return self.__acc_bal
#     def display(self):
#         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#         print("Name:",self.name)
#         print("Account type:",self.acc_type)
#         print("Account balance:",self.__acc_bal)
#         print("Account id:",self.acc_id)
#         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
# Syndicate=Bank()
# while True:
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Current Balance")
#     print("4. Display")
#     print("5. Exit")
#     choice=int(input("Enter the choice: "))
#     if choice==1:
#         Syndicate.withdraw()
#     elif choice==2:
#         Syndicate.deposit()
#     elif choice==3:
#         print("Current balance is",Syndicate.get_balance())
#     elif choice==4:
#         Syndicate.display()
#     else:
#         break
    
# Learn more about public and private data members
       
# Inheritance
# 1. Single level inheritance
# 2. Multiple level inheritance
# 3. Multi level inheritance

# public data member in inheritence is acessible on basis which class is calling the method
# private data member is not accessible in the child class
# protected data member is accessible in the child class
# super.__init__() is used to call the constructor of the parent class

# Example:
# class A: # Superclass Base Class Parent class
#     def __init__(self):
#         self.__a=10
#         self._b=20
#         self.x=3
#     def print_A(self):
#         self.__a=80
#         # self.__b=70
#         print(self.__a)
#         print("INSIDE PRINT A=",self._b)
#         print("INSIDE PRINT A=",self.x)
# class B(A): # Child Class Sub class
#     def __init__(self):
#         super().__init__()
#         self.c=5
#         self.d=10
#     def print_B(self):
#         print(self.c)
#         print(self.d)
#         print("INSIDE PRINT B.x=",self.x)# 7
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.e=0
#         self.f=-5
#     def print_C(self):
#         print(self.e)
#         print(self.f)
# C1=C()
# C1.print_C()
# C1.print_A()
# C1.print_B()

# class variable is shared between the objects of the class EX. count=0
# instance variable is specific to the object of the class EX. self.name="John"
# class variable is defined outside the __init__ method in the class
# instance variable is defined inside the __init__ method in the class

# Dunder methods : __init__(), __str__(), __add__(), __sub__(), __mul__(), __div__(), __mod__(), __pow__(),
# __eq__(), __lt__(), __gt__(), __le__(), __ge__(), __ne__(), __len__(), __getitem__(), __setitem__(), __delitem__(), 
# __iter__(), __next__(), __contains__(), __call__(), __enter__(), __exit__(), __new__(), __del__(), __repr__(), __hash__(),
# __bool__(), __format__(), __dir__(), __sizeof__(), __doc__()
# dunder methods are used to perform the operations on the objects of the class.
# these are the predefined methods in python

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return "Name: "+self.name+" Age: "+str(self.age)
#     def __repr__(self):
#         return "Name: "+self.name+" Age: "+str(self.age)
#     def __len__(self):
#         return len(self.name)
    
# P1=Person("John",25)
# P2=Person("Smith",30)
# print(P1)
# print(P2)   
# print(len(P1))
# print(len(P2))
# print(P1.__repr__())
# print(P2.__repr__())

# Operators:
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y    
#     def __add__(self,other):
#         return Point(self.x+other.x,self.y+other.y)
#     def __sub__(self,other):
#         return Point(self.x-other.x,self.y-other.y)
    
# P1 = Point(1, 2)
# P2 = Point(3, 4)
# P3 = P1 + P2
# P4 = P1 - P2
# print(f"P3: ({P3.x}, {P3.y})")
# print(f"P4: ({P4.x}, {P4.y})")

# Give me a example on getitem and setitem
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __getitem__(self,index):
#         if index==0:
#             return self.x
#         elif index==1:
#             return self.y
#         else:
#             return "Invalid index"
#     def __setitem__(self,index,value):
#         if index==0:
#             self.x=value
#         elif index==1:
#             self.y=value
#         else:
#             print("Invalid index")
# P1=Point(1,2)
# print(P1[0])
# print(P1[1])
# P1[0]=5
# P1[1]=10
# print(P1[0])
# print(P1[1])

# iterator and iterable
# __iter__() - Returns the iterator object itself. This is used in for and in statements.
# __next__() - Returns the next value from the iterator. This is used in for and in statements.
# StopIteration - Raises an exception to end the iteration.

# Lazy evaluation - It is a technique in which the evaluation of the expression is delayed until its value is actually required.
# my_list=[1,2,3,4,5]
# sum=0
# iterator = iter(my_list)
# sum+=next(iterator)
# print(sum)
# sum+=next(iterator)
# print(sum)

# class EvenIterator:
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.index = 0
#     def __iter__(self): 
#         return self
#     def __next__(self):
#         while self.index < len(self.numbers):
#             num = self.numbers[self.index]
#             self.index += 1
#             if num % 2 == 0:
#                 return num
#         raise StopIteration
    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = EvenIterator(numbers)
# for numbers in even_numbers:
#     print(numbers)
    
    
# generators : Generators are a type of iterable, like lists or tuples. They yield one item at a time, and they are lazy evaluated.
# Generators are created using the yield keyword.   
# def my_gen():
#     n=1
#     print("This is printed first")
#     yield n   
#     n+=1
#     print("This is printed second")
#     yield n   
#     n+=1
#     print("This is printed third")
    
# P1=my_gen()
# print(next(P1))


# #fIBONACCI SERIES
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# F=fib()
# for i in range(10):
#     print(next(F))

# decorators : Decorators are a design pattern in Python that allows a user to add new 
# functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate. 

# def repeat(n): # Decorator function
#     def decorator(func): # Inner function
#         def wrapper(*args, **kwargs): # Wrapper function
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"Hello {name}")
    
# greet("John")

# File handling
# file=open("test.txt","w")
# file.write("Hello World")
# file.close()

# Binary file handling : is used to store the data in the binary format
# file=open("test.txt","wb")
# file.write(b"Hello World")
# file.close()

def copy_binary_file(source,destination):
    with open(source,"rb") as src:
        with open(destination,"wb") as dest:
            c=1
            while c==1:
                chunk = src.read(102400)# 100kb
                dest.write(chunk)
                c+=1
                break
            
            
copy_binary_file("test.txt","test1.txt")
