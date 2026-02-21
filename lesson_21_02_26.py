"""
def назва_функції(аргументи):
    код функції

назва_функції(значення)
"""

# # однорядковий коментар
# print('''
# однорядковий комента
# однорядковий коментар
# однорядковий коментар
# ''')

# def first_function():
#     print('Hello world')
#
# first_function()
# print(first_function)
# def second_function():
#     hello = "Hello goods"
#     return hello
# print(second_function)
# print(second_function())

# def hello(arg1, arg2):
#     return arg1 + arg2
# print(hello)
# print(hello("Hello" , "World"))
# print(hello(3,5))
# print(hello(input("arg_1-"), input("arg_2-")))
# x = "IT"
# y = "STEP"
# print(hello(x, y))




# def s_triangle(a,h):
#     s = .5 * a * h
#     return s
#
# print(f"плоша трикутника s = {s_triangle(5, 6)}")
# print(f"плоша трикутника s = {s_triangle(int(input('a=')), int(input('h=')))}")


# def calc(var1, var2, var3):
#     return var1 * var2 / 4 + var3 ** 1.5
# resout_1 = calc(1, 2, 3)
# print(f"resout_1 = {calc(1, 2 ,3)}")
# resout_2 = calc(var1=1, var2=2, var3=3)
# print(f"resout_2 = {calc(var1=1, var2=2, var3=3)}")
# resout_3 = calc(1, 2 , var3=3)
# print(f"resout_3 = {calc(1, 2 ,var3=3)}")



import random
def coin_simulator():
    coin = random.randint(0, 1)
    if coin == 0:
        print("Решка")
    else:
        print("Орел")
for i in range(5):
    coin_simulator()