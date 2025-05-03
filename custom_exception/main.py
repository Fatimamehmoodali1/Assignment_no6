class InvalidAgeError(Exception):
    pass  # Custom exception class

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted.")

# Example usage:
try:
    check_age(16)
except InvalidAgeError as e:
    print("Exception caught:", e)
