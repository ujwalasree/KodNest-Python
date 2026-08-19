class Student:
    def details(self, roll, name, age, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks

    def study(self):
        print(f"{self.name} is studying")


s1 = Student()
s2 = Student()

s1.details(11, "Amit", 22, 85)
s2.details(12, "Arun", 23, 90)

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