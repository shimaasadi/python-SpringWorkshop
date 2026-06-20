#الگویی به شکل زیر با ستاره‌ها بسازید که با گرفتن یک عدد فرد (مثل 7)، اینچنین شکلی چاپ کند :
#*******
# *****
#  ***
#   *
#  ***
# *****
#*******
#Write a program that receives an odd number from the user and prints the above star pattern using only while loops (do not use for loops). 
#For example, if the input is 7, the pattern should be displayed like above.

x = int(input("plz enter an odd number : "))

if x % 2 == 0:
    print("your number must be odd!")
else:
    s = x
    f = 0

    while s > 0:
        print(" " * f + "*" * s)
        s -= 2
        f += 1

    s = 3
    f -= 2

    while s <= x:
        print(" " * f + "*" * s)
        s += 2
        f -= 1
