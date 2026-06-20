#کدی بنویسید که فاکتوریل یک عدد را با استفاده از while محاسبه کند.
#Write a program that receives a number from the user and calculates its factorial using a while loop.

x = int(input("enter the number : "))
printvalue = x
y = 1

while 1 < x:
    y = y* x
    x -= 1

print(f"{printvalue}!= {y}")

#or
#x = int(input("enter the number : "))
#y = 1
#i = 1

#while i <= x:
#    y = y* i
#    i += 1

#print(f"{x}!= {y}")
