#برنامه ای بنویسید که دو عدد از کاربر دریافت کند و حاصل جمع ، تفریق ، ضرب و تقسیم آن دو عدد را با استفاده از تابع در خروجی نمایش دهد.
#Write a program that receives two numbers from the user and uses a function to calculate and display their sum, difference, product, and quotient.

def mathematical_operations(x,y):
    print(f"sum of these two number is : {x+y}")
    print(f"subtraction of these two number is : {x-y}")
    print(f"product of these two number is : {x*y}")
    print(f"quotient of these two number is : {x/y}")

print("plz input two number to get their sum, subtraction, product and quotient. ")
x=int(input("first number : "))
y=int(input("second number : "))
mathematical_operations(x,y)
