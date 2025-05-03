class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage:
m = Multiplier(5)

print("Is m callable?", callable(m))  # True
print("Result of calling m(10):", m(10))  # Equivalent to m.__call__(10)
