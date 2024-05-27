# Instance method
   - Instance methods are the most common type of methods in Python classes. 
   - They operate on instances of the class and can access and modify instance attributes.
   - Instance methods are defined without any decorators and typically take `self` as the first parameter, which refers to the instance itself.
   - To access the instance memebers an `object reference` is required.
   - First object of instance function is called `caller object` and other are called `parameters` while calling.  
   Example:
   ```python
   class MyClass:
       def __init__(self, x):
           self.x = x

       def instance_method(self):
           return self.x

   #creating an instance of class
   obj = MyClass(42)
   print(obj.instance_method()) #using the object reference here
   # Output: 42
   ```


```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def add(self, b):
        return self.x + b

# Creating an instance of the class
t = MyClass(10)

# Calling the instance method add() with an argument b
result = t.add(5) # here t is caller object is 5 is parameter
print(result)  # Output: 15
```


