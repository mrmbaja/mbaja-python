# inheritance
class Parent:
  def __init__(self,name,age):
    self.name = name
    self.age = age

class Child(Parent):
  def greet(self):
      return f"my name is {self.name}, i am {self.age} years old"
  #instance
Child=Child("Austine",30)
print(Child.greet())






