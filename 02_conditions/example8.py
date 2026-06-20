# برنامه ای بنویسید که 
#x
#را از ورودی دریافت کرده و 
#y
#را براساس شرایط زیر محاسبه کند.
#X<0 ---> y=5x-3
#X=0 ---> y=10
#x>0 ---> y=2x+1
#Write a program that takes x as input and computes the value of y based on the conditions given above.

x = float(input("Enter a number for x: "))

if x < 0:
    y = 5 * x - 3
elif x == 0:
    y = 10
else:
    y = 2 * x + 1

print("The value of y is:", y)
