#یک دیکشنری بسازید که نام ۵ دانشجو و نمره آنها را از کاربر دریافت کند. سپس میانگین نمرات کلاس را محاسبه و چاپ کنید.
#سپس در این برنامه، نام دانشجویی که بالاترین نمره را دارد، چاپ کنید. اگر دانشجویی نمره زیر 10 داشته باشد، کنار اسمش Failed چاپ کند.
#Write a program that creates a dictionary containing the names and grades of five students. 
#The program should receive each student's name and grade from the user, calculate and display the class average, 
#identify and print the name of the student with the highest grade, and print "Failed" next to the name of any student whose grade is below 10.

scores = {}

for i in range(5):
    name = input("plz enter student's name: ")
    grade = float(input("enter student's score: "))
    scores[name] = grade

total = 0
for name in scores:
    total += scores[name]

average = total / len(scores)
print("class average :", average)

#or: (for line 16 & 17)
#for grade in scores.values():
#    total += grade

top_name = ""
top_score = -1

for name in scores:
    if scores[name] > top_score:
        top_score = scores[name]
        top_name = name

print("Top student:", top_name)

#or : (instead of line 26 to 33)
#top_student = max(scores, key=scores.get)
#print("Top student:", top_student)

for name, grade in scores.items():
    if grade < 10:
        print(name, " has Failed")
