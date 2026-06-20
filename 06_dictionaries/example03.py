#لیست زیر را در نظر بگیرید.برنامه ای بنویسید که این لیست را به یک دیکشنری تبدیل کند، به طوری که میوه نام کلید و عدد موجودی(عدد روبرو) ، مقدار باشد.
#Given the following list of tuples, Write a program that converts this list into a dictionary where the fruit name is used as the key and the corresponding quantity is used as the value.
# [("apple", 3), ("banana", 7), ("orange", 2)]

data = [("apple", 3), ("banana", 7), ("orange", 2)]

fruits = {}

for item in data:
    name = item[0]
    number = item[1]
    fruits[name] = number

print(fruits)
