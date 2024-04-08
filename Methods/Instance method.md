# Instance method
   - Instance methods are the most common type of methods in Python classes.
   - They operate on instances of the class and can access and modify instance attributes.
   - Instance methods are defined without any decorators and typically take `self` as the first parameter, which refers to the instance itself.

   Example:
   ```python
   class MyClass:
       def __init__(self, x):
           self.x = x

       def instance_method(self):
           return self.x

   #creating an instance of class
   obj = MyClass(42)
   print(obj.instance_method())  # Output: 42
   ```

