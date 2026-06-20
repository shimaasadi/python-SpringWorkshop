#برنامه ای بنویسید که یک عدد سه رقمی از کاربر دریافت کند و وارون آن را چاپ کند.
#Write a program that receives a three-digit number from the user and prints its reverse.

x=int(input('enter the number :'))
rev=0

for i in range(3):
    a=x%10
    rev =rev * 10 +a
    x=x//10

print(f'the reverse number is : {rev}')
