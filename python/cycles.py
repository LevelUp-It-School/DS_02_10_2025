# # in

# text = input()

# if "добр" in text:
#     print("Встретилось доброе слово")
# else:
#     print("Добрых слов не найдено")


# m = 12
# n = 19
# k = 25

# print(max(m, n, k))
# print(min(m, n, k))

# print(len("Привет"))

# print(len(str(2 ** 2025)))


# saved_pwd = "right"

# while input("Введите свой пароль: ") != saved_pwd:
#     pass
# print("Пароль верный! Вход разрешен!")

# range(n) - от 0 до n-1
# range(4) - 0, 1, 2, 3
# range(k, n) - от k до n - 1 
# range(1, 5) - 1, 2, 3, 4
# range(k, n, s) - от k до n - 1 с шагом s
# range(1, 10, 2) - 1, 3, 5, 7, 9

# n = int(input("Введите количество чисел: "))
# for i in range(n):
#     print(i)

# n = int(input("Введите конец чисел: "))
# k = int(input("Введите начало: "))

# for i in range(k, n):
#     print(i)

# n = int(input("Введите конец чисел: "))
# for i in range(0, n + 1, 2):
#     print(i)

# n = int(input("Введите конец чисел: "))
# for i in range(n, -1, -1):
#     print(i)

# for i in range(1, 5, -1):
#     print(i)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i * j}")
    
# rows, cols = 3, 4


# for r in range(rows):
#     row_sum = 0
#     for c in range(cols):
#         value = r + c
#         row_sum += value #row_sum = row_sum + value
#         print(value)
#     print(f"сумма строки {row_sum}")

# saved_pwd = "right"
# while True:
#     if input("Введите свой пароль: ")  == saved_pwd:
#         print("Пароль принимается")
#         break

# is_twelve = False
# for i in range(1, 6):
#     for j in range(1, 6):
#         val = i * j
#         if val == 12:
#             print("Ого 12!")
#             is_twelve = True
#             break
#         print(f"{i} x {j} = {val}")
#     if is_twelve:
#         break
    
# for i in range(1, 6):
#     for j in range(1, 6):
#         val = i * j
#         if i == j:
#             continue
#         print(f"{i} x {j} = {val}")

# while input("Введите строку (СТОП для остановки)") != "СТОП":
#     pass
# else:
#     print("Цикл завершен")
# tries = 0
# while (text := input("Введите строку (СТОП для остановки)")) != "СТОП":
#     tries +=1
#     if tries == 3:
#         break
# else:
#     print("Цикл завершен")
        

# text = input()

# print(text[3])

# text = input("Введите строку: ")
# i = int(input("Введите индекс символа: "))
# if i < len(text):
#     print(text[i])
# else:
#     print("Индекс не входит")

# text = input()
# # print(text[len(text)-1])
# print(text[-1])

# text = input()
# for i in range(len(text)):
#     print(text[i].upper())

# text = input()
# for letter in text:
#     print(letter.upper())

text = 'Anton'

for i, letter in enumerate(text):
    print(i, letter)