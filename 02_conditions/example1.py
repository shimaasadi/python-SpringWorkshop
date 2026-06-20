#2- برنامه ای بنویسید که یک سال را از ورودی بگیرد و بررسی کند که آیا سال کبیسه است یا خیر
#Write a program that receives a year and determines whether it is a leap year or not.

year = int(input("plz enter the year"))

if (year % 4 == 0 and year % 100 != 0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")
