# Define a class for student objects
class Student:
    # Initialize the attributes of a student object
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    # Define a string representation of a student object
    def __str__(self):
        return f"{self.name} ({self.roll_number}) has CGPA {self.cgpa}"

# Define a function to sort a list of student objects based on their CGPA in descending order
def sort_students(students):
    # Use the built-in sorted function with a custom key function that returns the cgpa attribute of a student object
    return sorted(students, key=lambda student: student.cgpa, reverse=True)

# Test the function with different input lists of students
students1 = [Student("Alice", "A001", 9.5), Student("Bob", "B002", 8.7), Student("Charlie", "C003", 9.2)]
students2 = [Student("David", "D004", 7.8), Student("Eve", "E005", 8.9), Student("Frank", "F006", 8.3)]
students3 = [Student("Grace", "G007", 9.7), Student("Harry", "H008", 9.4), Student("Ivy", "I009", 9.6)]

# Print the sorted lists of students
print("Sorted list of students1:")
for student in sort_students(students1):
    print(student)

print("\nSorted list of students2:")
for student in sort_students(students2):
    print(student)

print("\nSorted list of students3:")
for student in sort_students(students3):
    print(student)