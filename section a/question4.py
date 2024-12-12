# (b)
#A class is an object constructor. it starts with a capital letter and its always in singular.

#  # 4(iii)
def sum_of_numbers():
   a = int(input("Enter the first number : "))
   b = int(input('Enter the second number :'))
   sum = a + b
   print(f"The sum of the numbers {a} and {b} is {sum}")
sum_of_numbers()


# 4(iv)
class Car:
    def _init_(self,brand , name, color):
       self.brand=brand
       self.name=name
       self.color=color
 
b2=Car("Toyota" , "Benz", "Black") 
print(b2.brand)
print(b2.name)
print(b2.color)




# 4(v)
class car:
    def _init_(self,start_engine):
       self.start_engine=start_engine
data = car("The engine of the car has started.")      
print(data.start_engine)