#7- برنامه ای بنویسید که دو عدد تحت عنوان اندازه های دو زاویه از ورودی دریافت کند و سپس بررسی کند که آیا این زوایا متمم هستند یا خیر؟
#Write a program that receives two angles and determines whether they are complementary angles or not.

x = float(input("plz enter the first angle"))
y = float(input("plz enetr the second number"))

if x + y == 90:
    print("complementary angle")
else:
    print("the two angles are not complement!")
