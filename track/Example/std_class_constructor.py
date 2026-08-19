'''class Student:
    def __init__(self, roll, name, age, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks
    
    # Add 'self' parameter here
    def study(self):
        print(f"{self.name} is studying")


roll1 = int(input())
name1 = input()
age1 = int(input())
marks1 = int(input())
s1 = Student(roll1, name1, age1, marks1)

roll2 = int(input())
name2 = input()
age2 = int(input())
marks2 = int(input())

s2 = Student(roll2, name2, age2, marks2)
# Call the method on the s1 object
print("Roll No:", s1.roll)
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)
s1.study()

print("Roll No:", s2.roll)
print("Name:", s2.name)
print("Age:", s2.age)
print("Marks:", s2.marks)
s2.study()
'''
"""
class Student:
    def __init__(self, roll, name, age, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks
    
    # Add 'self' parameter here
    def study(self):
        print(f"{self.name} is studying")

s1 = Student(11, "Amit", 22, 85)
s2 = Student(12, "Arun", 23, 90)

# Call the method on the s1 object

print("Roll No:", s1.roll)
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)
s1.study()

print("Roll No:", s2.roll)
print("Name:", s2.name)
print("Age:", s2.age)
print("Marks:", s2.marks)
s2.study()
"""
class Student:
    def __init__(self, roll, name, age, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks
    
    # Add 'self' parameter here
    def study(self):
        print(f"{self.name} is studying")


s1 = Student(int(input()), input(), int(input()), int(input()))

s2 = Student(int(input()), input(), int(input()), int(input()))
# Call the method on the s1 object
print("Roll No:", s1.roll)
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)
s1.study()

print("Roll No:", s2.roll)
print("Name:", s2.name)
print("Age:", s2.age)
print("Marks:", s2.marks)
s2.study()
