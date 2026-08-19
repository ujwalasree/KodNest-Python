class Std():
    def study(self):
        print(f"{self.name} is studying")

s1 = Std()
s1.roll = 11
s1.name = "Amit"
s1.age = 22
s1.marks = 85

print(f"Roll No : {s1.roll}")
print(f"Name : {s1.name}")
print(f"Age : {s1.age}")
print(f"Marks : {s1.marks}")
s1.study()

s2 = Std()
s2.roll = 12
s2.name = "Arun"
s2.age = 23
s2.marks = 90

print(f"Roll No : {s2.roll}")
print(f"Name : {s2.name}")
print(f"Age : {s2.age}")
print(f"Marks : {s2.marks}")
s2.study()