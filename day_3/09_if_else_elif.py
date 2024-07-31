student_age = input("enter student age")
student_age = int(student_age)
required_age = 5
required_age = int(required_age)


# check if the student is eligible for admission

if student_age < required_age:
    print("Student is not eligible for admission")
elif student_age >= required_age:
    print("student can join ")


# else:             #condition is not working with else
#     print("Student is not eligible for admission")
