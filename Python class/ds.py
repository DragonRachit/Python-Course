# List

# my_List=[1,2,3,4]
# my_List.append(8)
# my_List.pop()

# for i in range(len(my_List)):
#     print(my_List[i])


# Tuple

# admin=("Kushal", "Sufal")
# admin.append("rachit")
# for name in admin:
#     print(f"1 million rupee is given to {name}")
#     print("Welcome", name)




# class Animal:
#     def __init__(self, name):
#         self.name=name
    
#     def speak(self):
#         print(self.name)

# class Dog(Animal):
#     pass

# d1=Dog("Rex")
# d1.speak()

class Cat:
    def sound(self):
        print("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")

c1=Cat()
f1=Fox()

for animals in (c1,f1):
    animals.sound()