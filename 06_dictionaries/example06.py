#برنامه ای بنویسید که دو دیکشنری از نمرات امتحان اول و دوم را داشته باشد
#سپس بررسی کند که نمره ی کدام دانشجو در امتحان دوم بهتر شده است. فقط اسم دانشجویانی را چاپ کند که نمره یشان در امتحان دوم بیشتر از اول است.
#exam1 = {"Ali": 14, "Sara": 16, "Reza": 12, "Fatemeh": 17}
#exam2 = {"Ali": 16, "Sara": 15, "Reza": 10, "Fatemeh": 18}
#Given the above dictionaries containing students' scores from two exams
#Write a program that compares the scores of each student in the two exams and prints only the names of the students whose score in the second exam is higher than their score in the first exam.

exam1 = {"Ali": 14, "Sara": 16, "Reza": 12, "Fatemeh": 17}
exam2 = {"Ali": 16, "Sara": 15, "Reza": 10, "Fatemeh": 18}

print("Students who improved in the second exam:")
for name in exam1:
    if exam2[name] > exam1[name]:
        print(name)
