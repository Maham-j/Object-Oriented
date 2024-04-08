# Static Methods:
   - Static methods are standalone methods that are not bound to either the class or instances of the class.
   - They do not take any implicit first parameter (`self` or `cls`).
   - Static methods are defined using the `@staticmethod` decorator and are often used for utility functions or operations that do not require access to instance or class attributes.

   Example:
   ```python
   class MyClass:
       @staticmethod
       def static_method(x, y):
           return x + y

   print(MyClass.static_method(3, 4))  # Output: 7
   ```

