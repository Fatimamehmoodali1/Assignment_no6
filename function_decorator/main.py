def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Calling the original function
    return wrapper

@log_function_call  # Applying the decorator to say_hello()
def say_hello():
    print("Hello!")

# Example usage:
say_hello()
