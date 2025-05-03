class Student:
    def __init__(self, name, marks):
        self.name = name      # 'self' is used to initialize the instance variable 'name'
        self.marks = marks    # 'self' is used to initialize the instance variable 'marks'

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage:
student1 = Student("Fatima", 92)
student1.display()
