#برنامه ای بنویسید که یک عدد تصادفی بین 1 تا 10 تولید کند و کاربر سعی کند آن عدد را حدس بزند. اگر درست حدس زد، به کاربر اطلاع دهید و اگر عددش یک واحد بزرگ تر یا کوچکتر بود، کاربر را مطلع کنید که حدسش نزدیک بوده و اگر حدس کاربر به کل درست نبود پیغام مناسب نمایش داده شود.
#Write a program that generates a random integer between 1 and 10. The user is then asked to guess the generated number. If the guess is correct, display a message indicating success. If the guessed number differs from the generated number by only one, inform the user that the guess was close. Otherwise, display an appropriate message indicating that the guess was incorrect.

#With random

import random

computerguess = random.randint(1, 10)
userguess = int(input("what's your guess?"))

if userguess == computerguess:
    print("congrats! you got it ")
elif (computerguess == 1 + userguess) or (computerguess == -1 + userguess):
    print("you were so close!")
else:
    print("sorry! the number was ", computerguess)
