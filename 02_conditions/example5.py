#6-برنامه ای بنویسید که 
#x
#را از کاربر دریافت کرده و قدرمطلق آن را چاپ کند.
#Write a program that receives x from the user and prints its absolute value.

x = float(input("plz enter the number"))

if x < 0:
    print(-1 * x)
else:
    print("ur number is positive")
