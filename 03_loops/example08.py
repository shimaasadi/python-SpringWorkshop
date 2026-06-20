#برنامه ای بنویسید که جدول ضرب را محاسبه و چاپ کند.
#Write a program that calculates and prints the multiplication table from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
