#برنامه ای بنویسید که از کاربر 5 عدد دریافت کند و تعداد اعداد زوج میان آنها را در خروجی نمایش دهد.
#Write a program that receives 5 numbers from the user and displays the number of even values among them.

count=0
for i in range(5):
    x=int(input(f'plz enter number{i+1}'))
    if x%2==0 :
        count+=1

print(f'there has been {count} even number in the list you entered')
