# Day 1

# print("Hello World")


# Integer, String, Boolean, Float, Complex

# name="Rachit"
# age=25
# salary=245.23
# com=3+5j
# b=True

# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(com))
# print(type(b))
# print()
# print(name)
# print(age)
# print(salary)
# print(com)
# print(b)


# Conditional Statements

# age=18

# if age >=18:
#     print("You are an adult")
# else:
#     print("You are a minor")


a=10
# if a>0:
#     print(f"{a} is positive")
# elif a<0:
#     print(f"{a} is negative")
# else:
#     print(f"{a} is zero")

# if a>0:
#     print(f"{a} is positive")
# if a<0:
#     print(f"{a} is negative")
# else:
#     print(f"{a} is zero")


# Loop

# For Loop
# While Loop

# for i in range(5,-1,-1):
#     print(i)


# i=10
# while i>0:
#     print(i)
#     i-=1


# num=int(input("Enter the number: \n"))
# for i in range(num+1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()

# name=input("Enter your Name: \n")
# age=int(input("Enter your age: \n"))
# print(f"Hello {name}")
# print(f"You are {age} years old.")
# print(f"You will be {age+1} years old next year")


# PYDANTIC MODULE
# name:str=input("Enter your Name: \n") # Pydantic module example here
# age:int=int(input("Enter your age: \n"))
# print(f"Hello {name}")
# print(f"You are {age} years old.")
# print(f"You will be {age+1} years old next year")



# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.__age=age # Protected(Private) attributes
#     def show_age(self):
#         return self.__age # Only access within class

# p1= Person("Rachit", 12)
# print(p1.name)
# print(p1.show_age())


# class Employee:
#     def __init__(self, salary):
#         self.__salary=salary
    
#     def get_salary(self):
#         return self.__salary


