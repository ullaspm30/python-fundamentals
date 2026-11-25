# Working with Lists and Dictionaries

# List example
skills = ["Python", "Git", "SQL", "System Design"]
skills.append("Cloud Basics")
print("My Skills:", skills)

# Dictionary example
profile = {
    "name": "Learner",
    "goal": "AI Systems Engineer",
    "location": "Bangalore",
    "year": 2026
}

print("\nProfile:")
for key, value in profile.items():
    print(f"{key}: {value}")