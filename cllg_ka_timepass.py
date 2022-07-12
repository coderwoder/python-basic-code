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
