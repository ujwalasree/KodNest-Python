class Student:
    def details(self, roll, name, age, marks):
        self.__roll = roll
        self.name = name
        self.age = age
        self.marks = marks

    def study(self):
        print(f"{self.name} is studying")
    
    def set_meth(self, new_roll):
        self.__roll = new_roll
    
    def get_meth(self):
        return self.__roll


s1 = Student()
s2 = Student()

s1.details(int(input()), input(), int(input()), int(input()))
s2.details(int(input()), input(), int(input()), int(input()))

print("Roll No:", s1.get_meth())
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)
s1.study()


print("Roll No:", s2.get_meth())
print("Name:", s2.name)
print("Age:", s2.age)
print("Marks:", s2.marks)
s2.study()