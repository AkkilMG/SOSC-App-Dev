def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before the function execution.")
        result = original_function(*args, **kwargs)
        print("After the function execution.")
        return result
    return wrapper_function


@decorator_function
def greet(name):
    print("Hello,", name)


@decorator_function
def add_numbers(a, b):
    return a + b


greet("HARSHITH_N")
result = add_numbers(2, 3)
print("Result:", result)

# Before the function execution.
# Hello, HARSHITH_N
# After the function execution.
# Before the function execution.
# Result: 5
