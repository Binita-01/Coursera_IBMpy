
class Car:
  max_speed = 120
  # this attribute is shared by all instances
  # __init__ method aslo known as the constructor
  # self parameter is the first parameter of the constructor, referring to the instance being crreated
  def __init__(self,speed,mileage):
    self.spedd = speed
    self.mileage=mileage
  def accelerate(self,acceleration):
    if self.speed + acceleration <= max_speed:
      self.speed += acceleration
    else:
      self.speed= Car.max_speed
      
  def get_speed(self):
    return self.speed
    
# calling methods on objects

# using dot notation
# res1 = obj.method(par1,par2)

# assigning obj methods to vars
# method_ref = obj1.method1
# res2 = method_ref(par1,par2)

# LAB
# #Type your code here
# dir(Car) gives the default methods for a class

