# class Rachit:
#     def __init__(mero,name, age):
#         self.name=name
#         self.age=age


#     def hello(self):
#         print("Hello")

# r1=Rachit()
# r1.hello()


# class Person:
#     name=""
#     age=0
#     city=""

# p1=Person()
# p1.name="Rachit"
# p1.age=12

# print(p1.name)



class learn:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # Private property
    
    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        self.__age=new_age

    def vote(self):
        if self.get_age() >= 18:
            print(f"Can vote {self.get_age()}")
        

p1=learn("Nice", 20)
# print(p1.get_age())
# print(p1._learn__age) # name mangling concept


p1.set_age(18)
p1.vote()



