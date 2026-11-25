# Writing to a file
with open("sample_data.txt", "w") as file:
    file.write("Name: Learner\n")
    file.write("Goal: Become AI Systems Engineer\n")
    file.write("Location: Bangalore\n")

# Reading from the file
print("Reading the file content:\n")
with open("sample_data.txt", "r") as file:
    content = file.read()
    print(content)