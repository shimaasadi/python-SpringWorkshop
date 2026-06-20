#برنامه ای بنویسید که دو عدد و یکی از عملگرهای + و – و * و / را از کاربر بگیرد 
#و عمل لازم باتوجه به عملگر انتخابی کاربر روی دو عدد انجام شود و نتیجه را چاپ کند. (برای مثال کاربر عدد 3 و 4 و همچنین عملگر + را وارد می کند و 7 نمایش داده می شود)
#Write a program that takes two numbers and an arithmetic operator (+, -, *, or /) as input from the user. 
#According to the operator entered, perform the appropriate arithmetic operation on the two numbers and display the result. 
#For instance, if the user enters 3, 4, and the + operator, the program should output 7.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operator!"

print("Result:", result)
