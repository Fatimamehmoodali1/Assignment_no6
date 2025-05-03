class Logger:
    def __init__(self):
        print("Logger started...")  # Constructor message

    def __del__(self):
        print("Logger stopped...")  # Destructor message

# Example usage:
log = Logger()
del log  # Explicitly deleting the object to call the destructor
