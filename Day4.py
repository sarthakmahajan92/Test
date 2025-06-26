
# try:
#     result = 10/ int(input("Enter the number:"))
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# else:
#     print("The result is:", result)
# finally:
#     print("End")



# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# else:
#     print("The result is:", result)
# finally:
#     print("End")

# Define the custom exception


class Error(Exception):
    """Custom exception for division errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Function that may raise the custom exception
def divide(a, b):
    if b == 0:
        raise Error("Cannot divide by zero!")
    return a / b

# Try-except block to handle the custom exception
try:
    result = divide(10, 0)
except Error as e:
    print(f"Custom Error Caught: {e}")
else:
    print(f"Result is: {result}")
