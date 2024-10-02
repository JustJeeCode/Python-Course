# Class variables = shared among all instances of a class
#					defined outside the constructor
#					allow you to share data among all objects created from that class


class Student:

	class_year = 2024
	num_students = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.num_students += 1


student1 = Student("John", 21)
student2 = Student("Tom", 23)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)

# print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)