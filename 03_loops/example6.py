#برنامه ای بنویسید که یک عدد از کاربر(مهم نیست چند رقمی) دریافت کند و وارون آن را در خروجی نمایش دهد
#Write a program that accepts an integer of any length from the user and displays the reverse of that number. For example, the reverse of 154 is 451.

digits= int(input('How many digits does your number have?'))
x=int(input('enter the number :'))
rev=0

for i in range(digits):
    a=x%10
    rev =rev * 10 +a
    x=x//10

print(f'the reverse number is : {rev}')
