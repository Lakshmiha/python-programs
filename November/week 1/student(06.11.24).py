student={}
student["Name"]=input("Enter the name:")
student["Roll_no"]=input("Enter rollno:")
student["Reg_no"]=input("Enter the reg no:")
student["Dept"]=input("Enter the department:")
student["Semester"]=input("Enter the semester:")
print("Student details=",student)
print()


student["total_marks"]=int(input("Enter the marks out of 100:"))
print()
print("dictionary after adding marks:",student)
print()



if student["total_marks"]>=90:
    student["grade"]="A"
elif student["total_marks"]>=82:
    student["grade"]="B"
elif student["total_marks"]>=75:
    student["grade"]="C"
elif student["total_marks"]>=60:
    student["grade"]="D"
elif student["total_marks"]>=50:
    student["grade"]="P"
else:
    del student["Roll_no"]

print("dictionary after removing Roll_no:",student)
print()
