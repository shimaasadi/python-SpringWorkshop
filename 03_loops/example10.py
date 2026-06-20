#برنامه ای بنویسید که یک عدد از کاربر دریافت کند و مشخص کند که عدد اول است یا خیر.
#Write a program that receives a number from the user and determines whether it is a prime number.

num = int(input('plz enter the number'))

if num <= 1:
    print('number is not a prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            print('number is not a prime number')
            break

    else:
        print('your number is a prime number!')
