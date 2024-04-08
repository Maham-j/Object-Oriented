# Object Oriented Programming
`Object Oriented Programming` is a programming model that uses the concept of ``object``.In Python everything is an object,and OOP helps in structuring code.

## Upsides:
- To increase the code readability.  
- Create objects that contain both data and functions.
- Facilitates code organization and maintenance.  
- The code executes from Bottom to Top.


# Class:
- `Classes` are the blueprints from which the objects are  created.
- They serve as the template for the objects and define their structure.  
- It tells how the object will look like.  
- It has atrributes (the characteristics an object will have) and methods (which functions an object can perform).
- The attributes and methods  maybe public, private or protected and can be accessed by dot(.).

  **Class Example**:
   ```python
   class Car:
       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year
       
       def display_info(self):
           print(f"Car: {self.make} {self.model} {self.year}")
   
   # Create an instance of the Car class
   my_car = Car("Toyota", "Camry", 2020)
   my_car.display_info()  # Output: Car: Toyota Camry 2020
   ```


# Object:
An `object` is an instance of a class, representing a specific entity.It has:    
-  state&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==>&nbsp;&nbsp;&nbsp;&nbsp;attribute/property.  
-  behaviour&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==>&nbsp;&nbsp;&nbsp;&nbsp;method.  
-  identity&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==>&nbsp;&nbsp;&nbsp;&nbsp;name.

   **Object Example**:
   ```python
   class Dog:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   
   # Create two instances of the Dog class
   dog1 = Dog("Buddy", 5)
   dog2 = Dog("Max", 3)
   
   print(f"{dog1.name} is {dog1.age} years old.")
   print(f"{dog2.name} is {dog2.age} years old.")
   ```


# Self:
`self` is a variable name used in Python methods to reference the instance of the class.
-  Like the pointers in C++.  
-  It binds the attributes with the arguments.  
-  It provides access to attibutes and methods.

  **Self Example**:
   ```python
   class Rectangle:
       def __init__(self, length, width):
           self.length = length
           self.width = width
   
       def area(self):
           return self.length * self.width
   
   # Create an instance of the Rectangle class
   rect = Rectangle(5, 3)
   
   print("Length:", rect.length)
   print("Width:", rect.width)
   print("Area:", rect.area())
   ```

  
