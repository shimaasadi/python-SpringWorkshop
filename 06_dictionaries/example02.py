#برنامه ای بنویسید که یک جمله با حروف کوچک (بدون نقطه در پایان خط) از ورودی بگیرد و تعداد تکرار هر کلمه را نمایش دهد.
#Write a program that receives a sentence written in lowercase letters (without a period at the end). The program should count and display how many times each word appears in the sentence.

sentence = input("plz enter a sentence: ")

words = sentence.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for word in counts:
    print(word, ":", counts[word])
