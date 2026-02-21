# name = input("Enter your name: ")
#
# age = input("Enter your age: ")
#
# print(f"Hello {name}, you are {age} old")








# age = int(input("Enter your age:"))
#
# if age > 17:
#     print("Вхід дозволено!")
# else:
#     print("Вхід заборонено!")








# import random
# while True:
#     secret_number = random.randint(1,10)
#     attempts = 3
#     print("Гра 'Вгадай число'!")
#     print("Я загадав число від 1 до 10. У тебе є 3 спроби.")
#     for i in range(attempts):
#         guess = int(input("Введіть число:"))
#         if guess == secret_number:
#             print("Вітаю! Ви вгадали число!")
#             break
#         elif guess > secret_number:
#             print("Менше")
#         else:
#             print("Більше")
#     else:
#         print("Спроби закінчилися! Загадане число було:", secret_number)
#     again = input("Ти хочеш грати знову? (так/ні):").lower()
#     if again != "так":
#         print("Гру завершено.")
#         break







# start = int(input("Введіть початкове число (з): "))
# end = int(input("Введіть кінцеве число (по): "))
#
#
# for number in range(start, end + 1):
#     print(number)

# n = int(input("Enter number:"))
# for i in range(n,0,-1):
#     if i % 2==0 :
#         print(i, end=" ")





# n = int(input("Введіть число : "))
#
# result = 1
#
# for i in range(1, n + 1):
#     result *= i
#
# print("Факторіал =", result)






# x = int(input("Вседите первое чесло "))
# y = int(input("Вседите второе чесло "))
# operation = input("Выбери действие (+,-,/,*): ")
# if operation == "+":
#     print(x+y)
# elif operation == "-":
#     print(x-y)
# elif operation == "*":
#     print(x*y)
# elif operation == "/":
#     if y != 0:
#         print(x / y)
#     else:
#         print("Нельзя делить на 0!")
# else:
#     print("Ошибка")
