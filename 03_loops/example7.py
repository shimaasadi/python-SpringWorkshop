#برنامه ای بنویسید که یک کلمه از کاربر دریافت کند و تعداد حروف صدادار را نمایش دهد. 
#Write a program that receives a word from the user and displays the number of vowels in it. (Vowels: a, e, i, o, u)

word =input('enter the word you wanna check')
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("number of vowels in the word :", count)
