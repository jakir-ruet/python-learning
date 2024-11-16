### Function
A function is a block of reusable code that performs a specific task. Functions allow you to organize your code, make it more modular, and avoid repetition. Functions can take inputs, process them, and return outputs.

**Types**
Four types function such as 
- Builtin, 
- User Define, 
- Lamda amd 
- Recursive function

**Higher Order Functions**
Functions can also be passed as arguments to other functions, or they can return other functions. This is called higher-order functions.

**Part**
Four part in a function such as function 
- Name, 
- Parameter list, 
- Body and 
- Return statement

Terms **argument** and **parameter** are closely related, but they refer to **different** concepts. Understanding the distinction between them is essential for working with functions.

- **Parameter:** A parameter is a variable defined in the function definition. It acts as a placeholder for the value that will be passed to the function when it is called. Parameters are part of the function's signature and specify what kind of input the function expects.
- **Argument:** An argument is the actual value you pass to the function when you call it. It is the input provided to the function in place of the parameter. Arguments can be literals, variables, or even expressions.
```bash
def greet(name="Guest"):  # 'name' is a parameter with a default value
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!  (No argument passed)
greet("Alice")  # Output: Hello, Alice!  (Argument passed)
```
#### From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that are sent to the function when it is called.

**Key Difference**
| **Parameter**                                                               | **Argument**                                                                            |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| A **parameter** is a variable in the function definition.                   | An **argument** is the actual value passed to the function when it is called.           |
| It acts as a placeholder for the value that will be passed to the function. | It is the input value provided to the function during the function call.                |
| Example: `def greet(name):` (`name` is a parameter)                         | Example: `greet("Alice")` ("Alice" is an argument)                                      |
| Parameters are defined in the function signature.                           | Arguments are passed during the function call.                                          |
| A function can have multiple parameters.                                    | A function can have multiple arguments corresponding to the parameters.                 |
| Parameters are used to specify what kind of input the function expects.     | Arguments are the actual values used to populate the parameters when the function runs. |
