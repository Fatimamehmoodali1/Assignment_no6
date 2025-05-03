class Bank:
    bank_name = "Old Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Changing the class variable

# Example usage:
bank1 = Bank()
print(bank1.bank_name)  # Prints "Old Bank"

# Change the bank name using class method
Bank.change_bank_name("New Bank")

# Check after changing the bank name
print(bank1.bank_name)  # Prints "New Bank"
bank2 = Bank()
print(bank2.bank_name)  # Prints "New Bank" (affected all instances)
