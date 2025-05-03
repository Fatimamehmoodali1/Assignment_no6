class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected (by convention)
        self.__ssn = ssn        # Private

# Creating object
emp = Employee("Fatima", 50000, "123-45-6789")

# Accessing variables
print("Public Name:", emp.name)         # Accessible
print("Protected Salary:", emp._salary) # Accessible but should be treated as protected
# print("Private SSN:", emp.__ssn)      # Will raise an error (uncomment to see)

# Accessing private variable using name mangling
print("Private SSN (using name mangling):", emp._Employee__ssn)
