#برنامه ای بنویسید که با استفاده از تابع، مشخص کند عددی که از کاربر دریافت شده اول است یا خیر.
#Write a program that uses a function to determine whether a number entered by the user is a prime number or not. The function should return an appropriate message indicating the result.

def prime(x):
    if x < 2:
        return(f"{x} is not a prime number!")

    for i in range(2, x):
        if x % i == 0:
            return(f"{x} is not a prime number!")
    return(f"{x} is a prime number.")

x = int(input("Please enter a number to check if it's a prime number: "))
a=prime(x)
print(a)
