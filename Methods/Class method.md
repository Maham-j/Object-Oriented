# Class Methods:
   - Class methods are methods that are bound to the class itself rather than to instances of the class. 
   - They can access and modify class-level attributes and perform operations that are relevant to the class as a whole.
   - Class methods are defined using the `@classmethod` decorator, and typically take `cls` as the first parameter, which refers to the class itself.
   - At class level the data mebers are usually private while the function members are usually public.  

   Example:
   ```python
   class MyClass:
       class_attribute = 42

       @classmethod
       def class_method(cls):
           return cls.class_attribute

   print(MyClass.class_method())  # Output: 42
   ```



```python
#To access the class members we use the class reference
class MyClass:
       class_attribute = 42
print(MyClass.class_attribute)    # Output: 42
```
