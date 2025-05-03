class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: uses existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        print(f"Employee: {self.employee.name}")

# Example usage:
emp = Employee("Fatima")
dept = Department("HR", emp)
dept.show_details()
