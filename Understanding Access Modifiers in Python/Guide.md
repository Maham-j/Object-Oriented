# Access Modifiers in Python Classes

Access modifiers are used to restrict access to methods and attributes of a class. Most programming languages have three types of modifiers:

- Public Access Modifiers
- Private Access Modifiers
- Protected Access Modifiers

# Public Access Modifiers:

All data members and function members of a class are public by default. They can be accessed everywhere in class or outside of the class, by `OBJECT  REFERENCE` or by `CLASS REFERENCE`.

```python
class Employee:
    def __init__(self):
        self.name = 'Maham'
        self.rollno = 'BSDSF22M008'
        
a = Employee()
print(f'Name:', a.name)
print(f'Rollno:', a.rollno)
```

Output:
```
    Name: Maham
    Rollno: BSDSF22M008
 ```

```python
class Employee:
    def __init__(self):
        self.name = 'Maham'
        
print(Employee().name)
```

Output: 
```
Maham
```

# Private Access Modifiers:

Private members are also called as dunders (double underscores) because they have double underscores in their names like `self.__name`. They can't be accessed outside of the class. If we want to access them, we have to create getter setters or by using class and a single leading underscore and a double leading underscore. This technique is called name mangling to protect the class private and subclass private attributes from being accidentally overwritten by a subclass.

```python
class Employee:
    def __init__(self):
        self.__name = 'Maham'
        self.__rollno = 'BSDSF22M008'
        
a = Employee()
print(a.name)  # This will cause an error because it can't be accessed directly

class Employee:
    def __init__(self):
        self.__name = 'Maham'
        
a = Employee()
print(a._Employee__name)
print(a._Employee__rollno)
```

Output:
```
Maham
BSDSF22M008
```


```python
class Employee:
    def __init__(self):
        self.__name = 'Maham'
        
    def setX(self, name):
        self.__name = name
        
    def getX(self):
        return self.__name
        
a = Employee()
print(a.getX())
```

Output: 
``` 
Maham
```

**Using `__dir__()` Method:**

A method called `dir()` which is used to see which methods can be applied to that object.

```python
class Employee:
    def __init__(self):
        self.__name = 'Maham'
        
a = Employee()
print(a.__dir__())
```

Output: 
```List of methods and attributes
```

# Protected Access Modifiers:

Methods or attributes that are only accessed by its class or subclass. The syntax to write this is a variable name followed by a single underscore (`self._name`). It does not provide any protection or restrictions to methods or attributes and no mangling is done in it. We can access it by calling its name only.

```python
class Employee:
    def __init__(self):
        self._name = 'Maham'
        self._rollno = 'BSDSF22M008'
        
a = Employee()
print(a._name)
print(a._rollno)
```

Output: 
```
Maham
BSDSF22M008
```

## Summary
By understanding and utilizing access modifiers effectively, you can better control the accessibility and encapsulation of your Python class attributes and methods

