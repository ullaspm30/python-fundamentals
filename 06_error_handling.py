# Error Handling (try-except)

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Please enter numbers only"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "two"))