# from datetime import date
# today = date.today()
# c_year = int(today.strftime("%Y"))
# name = input("Enter Your Naam : ")
# age = int(input("Enter Your Age : "))
# if age < 100:
#     print("You, My boy", name, "....if alive ,will turn 100 in year",
#           c_year+(100-age), ".")
# else:
#     print("Nani?! ...How are you alive??!!")

# n = int(input("Odd or Even , Let's check? "))
# print(f"This number {n} is Even") if n % 2 == 0 else print(
#     f"This number {n} is Odd")

# num = int(input("Set a Limit to your Fibonacci series : "))
# t = [0, 1]
# for i in range(num):
#     t_nxt = t[0]+t[1]
#     print(t_nxt, end=' ')
#     t[0] = t[1]
#     t[1] = t_nxt

# tum = input("TO reverse your number push it here : ")
# wum = tum[::-1]
# print(f"Your number {tum} reversed to {wum}", end=' ...')
# print("Is a palindrome") if tum == wum else print("Is not palindrome")

# Python program to check if the number is an Armstrong number or not

# num = int(input("Let's check your numbers Arms: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10

# print(num, "is an Armstrong number") if num == sum else print(
#     num, "is not an Armstrong number")

# ---------------
# import string
# alphabet = set(string.ascii_letters.lower())
# def pangram(con):
#     stri = ''
#     if len(set(con)) == len(alphabet):
#         stri = "this is a para"
#         return stri
#     else:
#         stri = "this is not a para"
#         return stri
# print("enter the sentence below :")
# state = input().lower()
# print(pangram(state))


# list_int = []
# list_int = input("Enter the list of integers : ").split()
# def histogram(pyapa):
#     for x in range(len(pyapa)):
#         print("*"*int(pyapa[x]))
# histogram(list_int)

# ----------------
# pending

# def length(c):
#     return len(c)


# char = input("Is you're input a string or list?").lower()

# if char == 'string':
#     str_li = input(f"Enter you're {char} : ")
#     print(f"The length of your {char} is {length(char)}")
# elif char == 'list':
#     str_li = list(input(f"Enter you're {char} : "))
#     print(f"The length of your {char} is {length(char.split(' '))}")
# # print(len(char))

# --------------------------
# def lesstf(a):
#     b = []
#     [b.append(x) for x in a if x < 6]
#     return b

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(lesstf(a))

# --------------------------
# dictu = {
#     'std1': 20,
#     'std2': 10,
#     'std3': 60,
#     'std4': 90,
# }


# def sorti():
#     sortedbyascending = sorted(dictu.items(), key=lambda t: t[1])
#     return sortedbyascending


# def sorty():
#     sortedbydecending = sorted(dictu.items(), key=lambda t: t[1], reverse=True)
#     return sortedbydecending


# print("Sorted by Ascending order", sorti())
# print("Sorted by Decending order", sorty())


# -----------------------------
# daic1 = {1: 10, 2: 20}
# dai2 = {3: 30, 4: 40}
# dc3 = {5: 50, 6: 60}
# d = daic1 | dai2 | dc3
# d = {**daic1, ** dai2, ** dc3}
# print(d)
# print(sum(d.values()))
# __________________PP Assignment___________________
# 1
# str = input("Enter a set of characters called as string, Of Your Choice : ")
# print(str[:2]+str[(len(str)-2):])

# 2
# string = "HEllo, This is a Test with no Marks   "
# print(f"'{string}'\nThe length of this string\nis {len(string)}")
# string = string.strip()
# print(f" REmoving blank space if any :\n'{string}'")
# sr = input("Now, Which Word do you want to search in this string? : ")
# print(f"yesss, '{sr}' is available") if sr in string else print(
#     f"Noooooooo, '{sr}' is unavailable")
# print("NOW more methods :")
# print(f"SLicinggg :\n'{string[6:]}'")
# print(f"reversinggg :\n'{string[::-1]}'")
# print(f"in upper case :\n'{string.upper()}'")
# print(f"Centering the string :\n'{string.center(len(string)+6,'*')}'")

# 3
# def firchar(str):
#     first_char = str[0]
#     str = str.replace(first_char, '$')
#     str = first_char+str[1:]
#     return str


# print("Enter a set of characters called as string, Of Your Choice : ")
# in_str = input()
# print(firchar(in_str))
