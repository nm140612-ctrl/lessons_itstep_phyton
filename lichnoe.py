

# step = input("Напишите что вам надо сделать через зарятую!:")
# step777_list = step.split(",")
# for u in range(len(step777_list)):
#     print(f" Шаг {u+1} : {step777_list[u]}")




# step1 = input("Напишите что вам надо сделать через '.' !:")
# step2_list = step1.split(".")
# for j in range(len(step2_list)):
#     print(f" {j+1} : {step2_list[j]}")







# import random
#
# while True:
#     play = input("Ты хочешь поиграть (да/нет): ").lower().strip()
#
#     if play != "да":
#         print("Пока")
#         break
#
#     print("Погнали!")
#     print("Я загадал число от 1 до 10!")
#
#     secret_num = random.randint(1, 10)
#     attempts = 3
#
#     for i in range(attempts):
#         guess = int(input("Введите число: "))
#
#         if guess == secret_num:
#             print("WIN!")
#             break
#         elif guess > secret_num:
#             print("Меньше")
#         else:
#             print("Больше")
#     else:
#         print("LOSE")
#         print("Число было:", secret_num)






# my_float: float = 1.50
# my_int = round(my_float)
#
# print(my_int)


# year = 2000
# if year % 4 == 0 and year % 100 != 0:
#     print("ЭТО ВЕСОКОСТНЫЙ ГОД!")
# elif year % 400 == 0:
#     print("ЭТО ВЕСОКОСТНЫЙ ГОД!")
# else:
#     print("ЭТО НЕ ВЕСОКОСТНЫЙ ГОД!"







x = int(input("Вседите первое чесло "))
y = int(input("Вседите второе чесло "))
operation = input("Выбери действие (+,-,/,*): ")
if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    if y != 0:
        print(x / y)
    else:
        print("Нельзя делить на 0!")
else:
    print("Ошибка")




# while True:
#     my_string = input("Enter a number:").strip()
#     if my_string.isdigit():
#         my_int = int(my_string)
#         print(my_int)
#         break
#     else:
#         print(f"{my_string} is not a number")








