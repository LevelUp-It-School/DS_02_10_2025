# numbers = []
# for i in range(5):
#     numbers.append(int(input()))

# print(numbers)

# numbers = [int(input()) for i in range(5)] 
# avg = sum(numbers) // len(numbers)
# numbers = [element for element in numbers if element > avg]
# print(numbers)


# numbers = (int(input()) for i in range(5))
# print(numbers)

# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)

# zeros = [[0] * 5] * 5
# zeros[0][0] = 1 
# print(zeros)

# zeros = [[0] * 5 for i in range(5)]
# print(zeros)
# zeros[0][0] = 1 
# print(zeros)

# for lst in zeros:
    # lst[1] = 5


# countries = {"Россия": ['русский'],
#             "Беларусь": ["белорусский", "русский"],
#             "Бельгия": ["немецкий","французский","нидерландский"]}
# mult_lang = [country for (country, lang) in countries.items() if len(lang) > 1]
# print(mult_lang)

# counries = {country: capital for country, capital in [("rus", "mow"), ("bel", "minsk")]}
# print(counries)


# def имя_функции(аргументы):
#     тело функции

# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True
# # print(only_even([2, 4, 6]))
# # print(only_even([2, 4, 6, 5]))
# print(numbers)


# def check_password(pwd):
#     return pwd == password

# password = "Python"
# print(check_password("Python"))

# def list_modify():
#     del sample[-1] 

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# def list_modify():
#     sample = [4, 5, 6]

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# def list_mod_1(list_arg):
#     list_arg = [1, 2, 3, 4]

# def list_mod_2(list_arg):
#     list_arg += [4]

# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]

# list_mod_1(sample_1)
# list_mod_2(sample_2)
# print(sample_1)
# print(sample_2)

# def inc():
#     global x
#     x += 1
#     print(f"Количество вызовов функции равно {x}")

# x = 0
# inc()
# inc()
# inc()


# def final_price(price, discount=1):
#     return price - price * discount / 100

# print(final_price(1000, 5))
# print(final_price(1000))

# def add_value(x, list_arg=[]):
#     list_arg += [x]
#     return list_arg
# print(add_value(0))
# print(add_value(0, [1,2,3]))
# print(add_value(1))

# def add_value(x, list_arg = None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg

# print(add_value(0))
# print(add_value(0, [1,2,3]))
# print(add_value(1))

# def final_price(price, discount=1):
#     return price - price * discount / 100

# print(final_price(1000, discount=5))
# print(final_price(discount=6, price=1000))


# def final_price(*prices, discount=1): #*args
#     return [price - price * discount / 100 for price in prices]

# print(final_price(1000, 500, 200, 50, 800, discount=5)) #(1000, 500, 200, 50, 800)

def final_price(*prices, discount=1, **kwargs):
    low = kwargs.get('price_low', min(prices))
    high = kwargs.get('price_high', max(prices))
    return [price - price * discount / 100 for price in prices if low <= price <= high]

print(final_price(1000, 500, 200, 50, 800, discount=5)) 
print(final_price(1000, 500, 200, 50, 800, discount=5, price_low=200))
print(final_price(1000, 500, 200, 50, 800, discount=5, price_high=500))
print(final_price(1000, 500, 200, 50, 800, discount=5, price_low=200, price_high=350))