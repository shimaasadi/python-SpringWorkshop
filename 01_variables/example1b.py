#1-برنامه ای بنویسید که دو عدد از کاربر دریافت کند و  
# عدد اول را در متغیر x
# و عدد دوم را در متغیر y
# قرار داده و سپس جای این دو مقدار را بدون استفاده از یک متغیر کمکی، جاجا کند
#Write a program that receives two numbers in variables x and y and swaps them without using a temporary variable.

x = int(input("Enter x: "))
y = int(input("Enter y: "))

x, y = y, x

print("x =", x)
print("y =", y)

#or
#x = float(input("plz enter ur first number. it'll be entered in x"))
#y = float(input("plz enter ur second number. it'll be entered in y"))

#x = x + y
#y = x - y
#x = x - y

#print("x=", x)
#print("y", y)
