#برنامه ای بنویسید که ابتدا از کاربر تعداد اعدادی که در نظر دارد وارد کند را دریافت کند و پس از دریافت آن اعداد تعداد اعداد زوج میان آنها را در خروجی نمایش دهد.
#Write a program that allows the user to specify how many numbers will be entered. 
#The program should then receive those numbers, determine how many of them are even, and display the count of even numbers. 
#Only the total count should be printed, not the even numbers themselves.

j=int(input('how many number you wanna enter?'))
count=0

for i in range(j):
    x=int(input(f'enter number {i+1}'))
    if x%2==0 :
        count+=1

print(f'there has been {count} even number in the list you entered')
