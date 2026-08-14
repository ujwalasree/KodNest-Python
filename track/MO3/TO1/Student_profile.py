class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills


student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
s = StudentProfile(student_id, name, course, experience, skills)

# Print the data stored in the object
print(f"Student ID: {s.student_id}")
print(f"Name: {s.name}")
print(f"Course: {s.course}")
print(f"Experience in Years: {s.experience}")
print(f"Skills: {', '.join(s.skills)}")