# ДЗ 8. Регулярні вирази
# Написати валідації за допомогою регулярних виразів:
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
import re
#
# li = ['+380699784503', '380678952364', '38012457', 'asd47552266++', '380645851', '+984561452332']
# print("Mobile phone list")
# print(li)
# print()
# for val in li:
#     if re.match(r'\+?\d{12}', val) and 12 <= len(val) <= 13:
#         print(val, 'correct')
#     else:
#         print(val, 'incorrect')
# print()

# # - домашній номер телефону (тільки цифри та довжина номера)

# li = ['2134256981', 'njjh4224545453443', '124545', '1234567891', '147258369', '+456789453215654']
# print("Phone list")
# print(li)
# print()
# for val in li:
#     if re.match(r'\d{10}', val) and len(val) == 10:
#         print(val, 'correct')
#     else:
#         print(val, 'incorrect')
# print()

#- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

# li = ['qwe---wrtq@gmail.com', '123123r3werfwefa', 'sdfasgsgsgas@gailcom', "sfa234543sfda@gmail.com",
#       "qwerwqer@ukr.net", "@gmail.com", "adahsdfukvasfgsadgfoasdgfaoisghdfiasgdgasf@gmail.com", "132@gmail.com"]
# print("Email list")
# print(li)
# print()
# for val in li:
#     if re.match(r'\w+[-_]*\w+@[a-zA-Z]{2,7}[.][a-zA-Z]{2,5}', val) and 15 < len(val) < 25:
#         print(val, "correct")
#     else:
#         print(val, "incorrect")

#- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# li = ["Гриб Олег Андрійович", "ЙЙЙЙййцйцуйцуйцу", "РРООЙ ооолі", "ф і в", "фівфівфівфівфвіфвфів фів фів"]
# print("ПІБ")
# print(li)
# print()
# for val in li:
#     if re.match(r'\w{2,10}\s\w{2,10}\s\w{2,10}', val) and 2 < len(val) <= 20:
#         print(val, "correct")
#     else:
#         print(val, "incorrect")