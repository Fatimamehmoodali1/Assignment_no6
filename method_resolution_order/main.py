class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass  # Inherits from both B and C

# Example usage:
obj = D()
obj.show()  # This will show the MRO result
