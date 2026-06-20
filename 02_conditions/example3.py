#4-برنامه‌ای بنویسید که ضرایب یک معادله درجه دوم 
#ax2+ bx +c =0 
#را بگیرد و با استفاده از فرمول دلتا، 
#مقدار x
#را محاسبه کند.
#Write a program that receives the coefficients of the quadratic equation ax² + bx + c = 0 and calculates the value(s) of x using the discriminant formula.

import math

print("welcome! plz keep this in mind; this is the usual form of equation that we consider ax2+bx+c=0")

a = float(input("plz enter a :"))
b = float(input("plz enter b :"))
c = float(input("plz enter c :"))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"your equation has two answers and they are: {x1}\t{x2}")

elif delta == 0:
    x = -b / (2 * a)
    print("your equation has one answer : ", x)

else:
    print("No solution!")
