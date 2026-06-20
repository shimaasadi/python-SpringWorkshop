#برنامه ای بنویسید که یک عدد تصادفی بین 1 تا 10 تولید کند و کاربر سعی کند آن عدد را حدس بزند. اگر درست حدس زد، به کاربر اطلاع دهید و اگر عددش یک واحد بزرگ تر یا کوچکتر بود، کاربر را مطلع کنید که حدسش نزدیک بوده و اگر حدس کاربر به کل درست نبود پیغام مناسب نمایش داده شود.
#Write a program that generates a random integer between 1 and 10. The user is then asked to guess the generated number. If the guess is correct, display a message indicating success. If the guessed number differs from the generated number by only one, inform the user that the guess was close. Otherwise, display an appropriate message indicating that the guess was incorrect.

#Without random

secret_num = 2
user_guess = int(input("what's your guees?"))

if user_guess == secret_num:
    print("congrats! you got it ")
elif (secret_num == 1 + user_guess) or (secret_num == -1 + user_guess):
    print("you were so close!")
else:
    print("sorry! the number was", secret_num)
