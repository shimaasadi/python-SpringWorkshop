#برنامه ای بنویسید که دو عدد را در متغیرهای A و B از کاربر دریافت کرده، سپس تمام اعداد فرد بین این دو عدد را در خروجی نمایش دهد.
#Write a program that receives two numbers in variables A and B from the user and prints all odd numbers between them.

a=int(input('plz enter your first number (a) :'))
b=int(input('plz enter your second number (b) :'))

if a > b:
    a, b = b, a

for i in range (a,b):
    if i%2 != 0 :
        print(i)
