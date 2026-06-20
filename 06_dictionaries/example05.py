#برنامه ای بنویسید که دیکشنری زیر از دانشجوها و رشته های موردعلاقه شان را داشته باشد
#سپس از کاربر نام یک دانشجو را بپرسد و رشته موردعلاقه ی او را چاپ کند. اگر نام وارد شده در لیست نباشد، پیغام مناسبی چاپ شود.
#سپس از کاربر بپرسد آیا می خواهد رشته موردعلاقه را تغییر دهد یا نه (no/yes) اگر yes وراد شد، مقدار جدید بگیرد و دیکشنری را به روزرسانی کند.
#Interests = {
#    "ali": "AI",
#    "sara": "web",
#    "reza": "game",
#    "Fatemeh": "AI"
#}
#Given the above dictionary that stores students and their fields of interest
#Write a program that asks the user to enter a student's name and displays that student's field of interest. 
#If the entered name does not exist in the dictionary, an appropriate message should be displayed. 
#Then ask the user whether they would like to change the student's field of interest (yes/no). If the answer is yes, receive the new value from the user and update the dictionary accordingly.

interests = {
    "ali": "AI",
    "sara": "web",
    "reza": "game",
    "Fatemeh": "AI"
    }

name = input('plz enter a student's name: ')

if name in interests:
    print("this student's favorite field is :", interests[name])

    answer = input("Do you want to update the interest? (yes/no): ")

    if answer == "yes":
        new_interest = input("Enter the new interest: ")
        interests[name] = new_interest
        print("Interest updated successfully.")
        print("Updated data :", interests)

    else:
        print("No changes made.")

else:
    print("Student not found.")
