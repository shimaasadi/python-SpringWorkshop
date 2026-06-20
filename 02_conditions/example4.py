#5-برنامه ای بنویسید که سه عدد  را از ورودی بگیرد و به ترتیب صعودی-نزولی آنها را چاپ کند.
#Write a program that receives three numbers and prints them in descending order.

num1 = float(input("plz enter the first number"))
num2 = float(input("plz enter the second number"))
num3 = float(input("plz enter the third number"))

if num2 > num1:
    temp = num1
    num1 = num2
    num2 = temp

if num1 < num3:
    temp = num1
    num1 = num3
    num3 = temp

if num2 < num3:
    num2 = num2 + num3
    num3 = num2 - num3
    num2 = num2 - num3

    # or:
    # x = num2
    # num2 = num3
    # num3 = x

print("ur numbers list in order is :", num1, num2, num3)
