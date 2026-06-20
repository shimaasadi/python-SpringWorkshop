#برنامه ای با شرایط زیربنویسید:
#فرض کنید ما موقعیت هایی از 1(شروع) تا 10 (پایان) داریم، شما باید از کاربر هر بار عدد بگیرید تا زمانی که کاربر به موقعیت 10 ام (مقصد) برسد
#و هر بار که کاربر موقعیت موردنظرش را وارد کرد؛ پیغامی تحت عنوان "شما در موقعیت ... هستید" برای کاربر چاپ بشود.
#به خاطر داشته باشید که در موقعیت 5 ام مانع وجود دارد و اگر کاربر 5 را وارد کرد باید پیغامی تحت عنوان " به مانع برخورد کردید! دوباره انتخاب کنید" نمایش دهید.
#You are moving along a path that contains positions numbered from 1 (start) to 10 (destination). 
#Repeatedly ask the user to enter a position until they reach position 10. 
#Each time a valid position is entered, display a message showing the user's current position. 
#Position 5 contains an obstacle; if the user selects position 5, display an obstacle warning message and ask them to choose again.

position = 1
goal = 10
obstacle = 5

print(" You are on a path from position 1 to 10.")
print(f" Be careful! There is an obstacle at position {obstacle}.\n")

while position < goal:
    print(f" You are currently at position {position}.")
    move = int(input(" Enter your next move (1-10): "))

    if move < 1 or move > 10:
        print(" Out of range! Please choose a position between 1 and 10.")
        continue

    if move == obstacle:
        print("You hit an obstacle! You can't go there. try again...")
        continue

    position = move

print(" You've reached your destination!")
