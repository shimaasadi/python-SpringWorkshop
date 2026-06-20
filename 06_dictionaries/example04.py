#یک دیکشنری بنویسید که کلید آن اسم دانشجو و مقدار آن لیستی از دروسی باشد که دانشجو انتخاب واحد کرده است. سپس:
#اسم دانشجویانی که درس پایتون را برداشته اند را چاپ کنید.
#نام درسی که بیشترین تعداد دانشجو آن را برداشته اند پیدا کنید.
#Create a dictionary in which each key represents a student's name and each value is a list of courses selected by that student. Then:
#A) Print the names of all students who have selected the course "python".
#B) Determine and print the course that has been selected by the largest number of students.

students = {
    "Ali": ["python", "algorithms", "programming"],
    "Sara": ["programming", "python", "AI"],
    "Reza": ["math", "AI"],
    "Fatemeh": ["math", "programming", "algorithms"],
}

print("Students who selected 'python':")
for name, courses in students.items():
    if "python" in courses:
        print(name)

count = {}

for courses in students.values():
    for course in courses:
        if course in count:
            count[course] += 1
        else:
            count[course] = 1

x = max(count, key=count.get)
print("Most selected course:", x)
