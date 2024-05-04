# Python Pickle Tutorial: Object Serialization
Discover the python ``pickle`` module: Serialization and Deserialization and much more!
Built-in module

# Intoduction to Object Serialization:
 Serialization involves preserving a data structure in memory to enable loading or transmission later without losing its current state. It is like arranging the date in the form of series (of bytes).<br /><br />
 
 Here is a diagram that simply explains how the process of serialization works!
![Alt text](https://github.com/Maham-j/Object-Oriented/blob/main/Pickle/Pickle_Python_Object_Serialization_c63df96c79.png)

In Python, working with high-level data structures like lists, tuples, and sets is common. However, to store these objects in memory, they must first be converted into a sequence of bytes understandable by the computer, a process known as ``Serialization``.<br />
When retrieving the same data structure later, these bytes are transformed back into the original object through ``Deserialization``.<br /> 
Serialization formats such as JSON, binary files, pickle objects, and   database  are available, each with its applications. <br /> <br /> <br /> <br /> 

# Why is Object Serialization Necessary?
Object serialization is important to understand before we start working with Python Pickle.<br />
Ever thought about why we can't simply save data structures in a text file for later use instead of serializing them?<br /><br />

Let's see an example that tells why it's important.<br /><br />

```python
# Nested Dictionary
data = {
    "name": "John",
    "age": 30,
    "pets": [
        {"name": "Fluffy", "species": "Cat"},
        {"name": "Buddy", "species": "Dog"}
    ]
}

# Writing data into a file without serialization
with open("data.txt", "w") as file:
    file.write(str(data))
```

In this example, we change the dictionary data into a string using `str()` and put it in a file, but it loses how things are connected and organized.
The resulting content in the "data.txt" file would be:

```
{'name': 'John', 'age': 30, 'pets': [{'name': 'Fluffy', 'species': 'Cat'}, {'name': 'Buddy', 'species': 'Dog'}]}
```

As you can see, the data is unstructured which will make it difficukt  when read back from the file.
This is where serialization comes in.<br /><br />

## Serialization helps keep the original form of complex data types like dictionaries, data frames, and nested lists intact, so no important details are lost when storing or sending them.
