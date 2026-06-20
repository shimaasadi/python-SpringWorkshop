#3-برنامه‌ای بنویسید که بررسی کند آیا یک عدد سه‌رقمی هم بر ۳ بخش‌پذیر است و هم رقم یکان آن ۷ است؟
#Write a program that checks whether a three-digit number is divisible by 3 and its last digit is 7.

num = int(input("plz enter a three-digit number "))

if (100 <= num <= 999 or -999 <= num <= -100) and num % 3 == 0 and num % 10 == 7:
    print("confirm")
else:
    print("ur number is not a three-digit number! plz try again")
