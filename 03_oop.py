class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"My name is {self.name} and I am learning {self.course}."

    def update_course(self, new_course):
        self.course = new_course
        return f"Course updated to {self.course}"

# Testing
student1 = Student("Rahul", "Information Science")
print(student1.introduce())
print(student1.update_course("AI Systems Engineering"))
print(student1.introduce())