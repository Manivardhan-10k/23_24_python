# class Greet:
#     morning="Good Morning!"
#     noon="Good Afternoon"
#     evening="Good night"
#     night="Good Night"

#     def greeting(name=""):
#         return f"hello {name}"

# print(Greet.night)
# print(Greet.greeting("mani"))






class Car:
    def __init__(self,name,brand,colour):  ##constructor function 
        self._name=name 
        self._brand=brand
        self._colour=colour      
    def details(self):
        return f"this is a {self._name} car from {self._brand} of color {self._colour}"
new_car=Car("fortuner","toyota","black")  
car2=Car("s-cross","suzuki","white")
print(new_car.details())
print(car2.details())





    
