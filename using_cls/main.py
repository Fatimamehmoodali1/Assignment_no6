class Counter:
    count = 0  # Class variable to keep track of the number of objects

    def __init__(self):
        Counter.count += 1  # Increment the count every time a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  # Display the number of objects created
