#برنامه‌ای بنویسید که یک پسورد از کاربر بگیرد به گونه ای که کاربر فقط 3 بار فرصت داشته باشد پسورد صحیح را وارد کند. 
#اگر پسورد صحیح وارد شود، بنویسد "خوش آمدید!" وگرنه بنویسد "دسترسی غیرمجاز". 
#پسورد صحیح = python123
#Write a program that asks the user to enter a password. The user should have only three attempts to enter the correct password. 
#If the correct password is entered, display a welcome message; otherwise, deny access after three failed attempts. 
#Assume that the correct password is python123.

pas = "python123"
count = 0

while count < 3:
    x = input(" plz enter your password : ")
    if x == pas:
        print("Login successful. Welcome!")
        break
    else:
        print("Incorrect password")
        count += 1

if count == 3:
    print("Access denied")
