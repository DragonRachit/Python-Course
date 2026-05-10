
# def area(a:int,b:int):# parameters
#     return a*b

# print(area(1,2))# arguments



# def chakki(grains:str):
#     return f"flour of {grains}"

# pithho=chakki("wheat")

# print(f"Making roti with {pithho}")



# def add_number(num1:int,num2:int):
#     return num1+num2

# def sub_number(num1:int,num2:int):
#     return num1-num2

# def multiply_number(num1:int,num2:int):
#     return num1*num2

# def divide_number(num1:int,num2:int):
#     return num1/num2

# def cin():
#     num1=int(input("Enter the number1: \n"))
#     num2=int(input("Enter the number2: \n"))
#     return num1,num2


# while True:
#     print("Menu")
#     print("1. Add")
#     print("2. Sub")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choosen=int(input("Choose the number:\n"))

#     if choosen==1:
#         num1,num2=cin()
#         print(add_number(num1,num2))
#     elif choosen==2:
#         num1,num2=cin()
#         print(sub_number(num1,num2))
#     elif choosen==3:
#         num1,num2=cin()
#         print(multiply_number(num1,num2))
#     elif choosen==4:
#         num1,num2=cin()
#         print(round(divide_number(num1,num2),2))
#     elif choosen==5:
#         print("Thanks")
#         break
#     else:
#         print("Choose the given number from above")

# numbers=[]

# def cin_list():
#     n=int(input("Enter the totoal numebr to store in a list: \n"))
#     for i in range(1,n+1):
#         give=int(input((f"Enter the number: {i}\n")))
#         numbers.append(give)
    
# def Total(num:list):
#     total=0
#     for i in num:
#         total+=i
#     return total

# def high(num:list):
#     high_num=num[0]
#     for i in num:
#         if i>high_num:
#             high_num=i
#     return high_num
    
# print("First Fill the Data Ask")
# cin_list()

# while True:
#     print("\nMenu")
#     print("1. Find SUM")
#     print("2. Find MAX")
#     print("3. Exit")

#     choosen=int(input("Choose the number:\n"))

#     if choosen==1:
#         print(f"Your total sum is : {Total(numbers)}")
#     elif choosen==2:
#         print(f"Highest number is : {high(numbers)}")
#     elif choosen==3:
#         print("Thanks")
#         break
#     else:
#         print("Choose the given number from above")



# try:
#     print(x)
# except Exception as error:
#     print(f"You got this {error}")
# finally:
#     print("I am Finally")

