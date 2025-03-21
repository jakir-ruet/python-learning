Classes are a way to define custom data types or blueprints for creating objects (instances). A class allows you to bundle data (attributes) and functionality (methods) together, making it a powerful concept for structuring and organizing code.
```bash
class ClassName:
    def `__init__`(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method_name(self):
        # Do something
        pass
```

**Components of a Python Class**
- `__init__()` method:
  - The `__init__` method is the constructor of the class. It is automatically called when an object of the class is created.
  - self is the first parameter of all instance methods (including `__init__`), and it refers to the instance of the class.
- Attributes:
  - These are the variables that belong to the class and are usually initialized in the `__init__` method. They store data about the object.
- Methods:
  - These are functions defined inside the class. They describe the behaviors or actions that can be performed on or by an object of the class.