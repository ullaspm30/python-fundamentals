def greet(name):
    return f"Hello, {name}! Welcome to AI Systems."

def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Testing the functions
print(greet("Learner"))
print("Sum:", add_numbers(15, 27))
print("Average:", calculate_average([10, 20, 30, 40]))