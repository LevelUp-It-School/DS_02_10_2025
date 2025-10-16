#коллекция[начало:конец:шаг]
# text = "Привет мир!"

# print(text[:5])
# print(text[::2])
# print(text[::-1])
# print(text[:-2])
# print(text[:-2:-1])

# print(text[8:11])
# print(text[8:])
# print(text[0::1])

# word = 'мир'
# word[0] = 'п'

numbers = [10, 20 , 30, 40, 50]
mixed_list = [10, 20.55, 'mama']

# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# numbers[2] = 100
# print(numbers)


# numbers = []
# for i in range(10):
#     numbers.append(int(input())) #имя_списка.append(элементь_для_добавления)

# print(numbers)

# numbers = [10, 20, 50]
# del numbers[-1]
# print(numbers)

# numbers = [10, 20, 50, 100, 150]
# del numbers[::2]
# print(numbers)

# print(10 in [1, 2, 3])
# print(10 not in [1, 2, 3])
# print([1, 2] + [3, 4, 5])
# print([1, 2, 3] * 5)
# print(len([1, 2, 3]))
# print(min([1, 2, 3]))
# print(max([1, 2, 3]))

# print([1,2,3,4,5,6,2].index(2))
# print([1,2,3,4,5,6,2,2,2].count(2))

# list_name = [1,2,3,4,5,6,2]
# list_name.clear()
# print(list_name)

# list_name = [1,2,3,4,5,6,2]
# list_copy = list_name.copy()
# list_copy_2 = list_name
# list_name.append(100)
# print(list_name)
# print(list_copy_2)
# print(list_copy)

# s = [1, 2, 3]
# t = [4, 5]
# s.extend(t) #  s+=t
# print(s)

# s = [1, 2, 3]
# s.insert(1, "hello")
# print(s)

# s = [1, 2, 3]
# print(s.pop())
# print(s)

# s = [1, 2, 3, 2, 1]
# s.remove(2)
# print(s)

# s = [1, 2, 3]
# s.reverse() # s = s[::-1]
# print(s)

# s = [212, 3445, 11, 34334, 220, 200]
# s.sort(reverse=True)
# print(s)

# s = [212, 3445, 11, 34334, 220, 200]
# new_s = sorted(s)
# print(s)
# print(new_s)


# s = [1, 2, 3, 2, 2, 5, 6]
# while 2 in s:
#     s.remove(2)
# print(s)

# numbers = (1, 2, 3, 4, 5)
# one_number = (1, )

# print(numbers)
# print(one_number)
# print(type(numbers))

# a = 1
# b = 2
# (a, b) = (b, a)
# print(f"a = {a}, b = {b}")

# text = "Hello world!"
# list_symbols = list(text)
# tuple_symbols = tuple(text)
# text_from_list = str(list_symbols)
# print(list_symbols)
# print(tuple_symbols)
# print(text_from_list)

# vowels = {'a', 'e', 'y', 'u', 'i', 'o', 'o', 'o'}
# print(vowels)
# print(type(vowels))

# empty_set = set()
# print(len(empty_set))

# word = 'collection'
# letters = set(word)
# print(letters)

# vowels = {'a', 'e', 'y', 'u', 'i', 'o', 'o', 'o'}
# letter = input()
# if letter.lower() in vowels:
#     print("Vowel")
# else:
#     print("Not vowel")

s_1 = {1, 2, 3}
s_2 = {3, 4, 5}
# s_union = s_1.union(s_2) #s_1 | s_2
# print(s_union)

# s_intersection = s_1.intersection(s_2) # s_1 & s_2
# print(s_intersection)

# s_dif = s_1.difference(s_2) # s_1 - s_2
# print(s_dif)

# s_sym_dif = s_1.symmetric_difference(s_2) #s_1 ^ s_2
# print(s_sym_dif)

# vowels = {'a', 'e', 'y', 'u', 'i', 'o', 'o', 'o'}
# letters = set("collection")
# print(",  ".join(letters & vowels))

# s_1 = {1, 2, 3}
# s_2 = {3, 2, 1}
# print(s_1 == s_2)

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2)

# s = set()
# s.add(1)
# print(s)

# s = {1, 2, 3}
# s.remove(2)
# print(s)

# s = {1, 2, 3}
# s.discard(5)
# print(s)

# countries_and_capitals = [("Россия", "Москва"), ("США", "Вашингтон")]
# for country in countries_and_capitals: 
#     if country[0] == "США":
#         print(country[1])
#         break

countries_and_capitals = {"Россия": "Москва",
                          "США":"Вашингтон",
                          "Франция": "Париж"}
# print(countries_and_capitals["США"])
# countries_and_capitals["Грузия"] = "Тбилиси"
# print(countries_and_capitals)
# if "Сербия" in countries_and_capitals:
#     print(countries_and_capitals["Сербия"])
# else:
#     print("Страна пока не добавлена в словарь")

# for country in countries_and_capitals:
#     print(country, countries_and_capitals[country])

# for k in countries_and_capitals.keys():
#     print(k)

# for v in countries_and_capitals.values():
#     print(v)

# for k, v in countries_and_capitals.items():
#     print(k, v)