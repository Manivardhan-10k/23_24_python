# OOPS:
# object oriented programming:

# classes: 

# objects :

# inheritance :

# polymorphism:

# encapsulation:

# abstraction:



# class:
#     it is a blue print or template to create objects:

# class Car:
#     brand="audi"   ##static variables
#     __private="secret"  ##private variable
#     def __init__(self,model,year,color):
#         self.__model=model   ##instance variable
#         self.year=year 
#         self.color=color
#     def start(self):
#         return f"{self.__model} is started"
#     def details(self):
#         return ( f"The car model is {self.__model} is of color{self.color}   made in year {self.year}")



# c1=Car()
# c2=Car()
# print(c1.name)
# print(c2.__private)

# c1=Car("a5",2024,"white")
# print(c1.start())
# print(c1.details())

# c2=Car("A7",2025,"silver")
# print(c2.start())
# print(c2.details())

# a class having the propeties of another class (parent class)

# class Animal:
#     speak="no"
#     makeSound="yes"

# class Dog(Animal):
#     def __init__(self,name):
#         self.name=name
#     def sayHello(self):
#         return f"hi my name is {self.name}"
        
# # class Cat:
# #     speak="no"
# #     makeSound="yes"
# jimmy=Dog("jimmy")
# print(jimmy.speak)
# print(jimmy.makeSound)
# print(jimmy.sayHello())


# polymorphism:


# class Cat:
#     def sound(self):
#         return "meow"
# class Dog:
#     def sound(self):
#         return "bow"

# c1=Dog()
# print(c1.sound())

# c2=Cat()
# print(c2.sound())



# class Animal:
#     def sound(self):
#         return "some sound"
# class Dog(Animal):
#     def sound(self):
#         return "bark"
# class Jimmy(Dog):
#     def sound(self):
#         return "woof"

# j=Jimmy()
# print(j.sound())

# method overloading 

# method overriding


# class Operations:

#     def add(self,a,b):
#         return a+b

# opr=Operations()
# print(opr.add("hi ","hello"))

# c c++ java


# f = open('sample.txt', 'r')
# print(f.read())