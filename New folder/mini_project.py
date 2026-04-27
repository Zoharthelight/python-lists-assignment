student = ["John Doe", 22, "Computer Science", 4.5, "Nigeria"]

print("Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])
print("CGPA:", student[3])
print("Country:", student[4])


student[2] = "Software Engineering"
student[3] = 4.8

print(student)

print(student[::-1])
print(student[:3])