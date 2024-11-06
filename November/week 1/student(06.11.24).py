student={"Name":"Arjun","Roll_no":"S101","Reg_no":"R1234","Dept":"Computer Science","Semester":1,"Marks":{"Maths":40,"Data Structures":30,"SE":20,"DFCA":20}}
total_marks=sum(student["Marks"].values())
if total_marks>=90:
    grade="A"
elif total_marks>=82:
    grade="B"
elif total_marks>=75:
    grade="C"
elif total_marks>=60:
    grade="D"
elif total_marks>=50:
    grade="P"
else:
    student.pop("Roll_no")

student["total_marks"]=total_marks
student["grade"]=grade
print("Updated Student Dictionary:")
for key,value in student.items():
    if key=="marks":
        print(f"{key}:{value}")
    else:
        print(f"{key}:{value}")
