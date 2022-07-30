# QUESTION SOLVING

# letter = '''\nDear,|name|
# Greetings from Abc  ,
# Happy to tell you that you are selected for bllah balh,
# regards, batetetete
# Date:|date|
# '''
# hello = "\\Dear ,\n \tdon\'t go to far\nthanks!\\ "
# a = input("enter your name please:\n")
# b = input("Enter your date:\n")
# a = a.capitalize()
# # cdb = "  "
# # cdb = cdb.count(cdb)
# letter = letter.replace("  ", " ")
# letter = letter.replace("|name|", a)
# letter = letter.replace("|date|", b)
# print(letter)
# print(hello)

# print('''Dear,''' + str(a)+'''\nyou are slected !\n''', b)

# --------------------------------------

# list

# l1 = [1, 2, 0]

# l1.sort()
# l1.reverse()

# l1.append(2.79)  # Append(adds) The number from The end of the list
# l1.extend(123) #Extend adds each element to the list as an individual element.
# The new length of the list is incremented by the number of elements added.

# l1.insert(0,"Ready")
# l2=len(l1)
# print(l1[:-1])
# l1.count() #Returns the number of elements with the specified value.
# del l1[1]  # deletes the element at index 1
# l1.pop(2)  # Removes & Returns the last element from the list
# l2=l1.pop(1)
# print(l2)
# l1.remove(0) #Removes the element passed to this method
# print(l1)

# li = input().strip()  #removes useless whitespaces
# li = input().splits() #splits them into sub strings

# tuple

# t = (1, 'ready', True, True, 2.9)
# # print(t.count(True))
# # print(t.index(1))
# t1 = len(t)
# print(t1)

# TEST
# f1 = []
# n = int(input("enter your number of fruits"))

# i = 1
# while(i <= n):
#     l2 = input("enter your fruits")
#     f1.append(l2)
#     i = i+1
# print(f1)


# f1 = []
# n = int(input("enter your number of students"))

# i = 1
# while(i <= n):
#     l2 = input("enter your marks")
#     f1.append(l2)
#     i = i+1
# f1.sort()
# print(f1)

# a = [12, 32]
# print(sum(a))  # without loop

# with loop
# n = len(a)
# sum = 0
# for x in range(n):  # x is i while range is i<=n whatever
#     sum += a[x]
# print(sum)

# withloop
# count = 0
# n = len(a)
# for x in range(n):
#     if a[x] == 0:
#         count += 1
#         print("counted")

#     else:
#         print("Not zero")
# print('%d\n' % (count))

#  withoutloop
# print(a.count(0))

# --------------------------------------

# DICTIONARY
# mynary = {
#     "fast": "in a Tez",
#     "marks": [12, 34, 56],
#     "anothernary": {"band": "bajadi"},
#     1: 2
# }

# def sort(): #sorting dictionary  by values
#     sortedbyascending = sorted(dictu.items(), key=lambda t: t[1])
#     print(sortedbyascending)

# print(list(mynary.keys()))
# print(mynary.values())
# print(mynary.items())
# update01 = {
#     "fast": "but no slow",
#     3: 4,
#     "slow": "hump"
# }
# mynary = update01 | mynary #addding two or more dictionaries together
# mynary.update(update01)
# print(mynary)
# print(mynary["fast2"])  # throws error
# print(mynary.get("fast2"))  # throws none


# SET no repetation and
# no adding list and dictionary since they can be changed
# set = {1, 2, 3, 4, 5, "6", 6}
# set = set()  # empty
# newset = (1, 2, 3, 4, 5)
# set.add(newset)
# # set.add(12.34)
# set.add(12.34)
# set.add(1.34)

# set.pop()  # random if blank
# set.remove(newset)
# # print(set)
# set.clear()
# print(set)

# TEST
# nary = {
#     "fast": "tez",
#     "slow": "bhuda",
#     "medium": "sadaran"
# }

# print("which of the following words you want to translate to")
# print(list(nary.keys()))
# inp = input("the word please?")
# print(nary.get(inp))

# set = set()
# for x in range(8):
#     n = input()
#     set.add(n)
# print(set)
# # print(sorted(set)) just in case
# set.add(20)
# set.add(20.22)
# set.add("20")
# print(len(set))

# dictionarys = {}
# a = ["1", "2"]
# b = [2, 3]
# dictionarys[a[0]] = b[0]
# print(dictionarys)

# a = []
# b = []
# for x in range(4):
#     x = input("Enter your name:")
#     y = input("Enter the language you love:")
#     a.append(x)
#     b.append(y)
#     print("-----------\n")

# dictnarys = {}
# for i in range(len(a)):
#     dictnarys[a[i]] = b[i]
# print(dictnarys)


# --------------------------------------

# IF AND ELSE

# a=[3,1,5,6]
# a = []
# for x in range(4):
#     n = input()
#     a.append(n)

# for x in range(len(a)):
#     if(a[0] < a[x]):
#         a[0] = a[x]

# print(a[0])


# num = int(input("Enter your Number of subjects:"))
# a = []  # Input
# for x in range(num):
#     n = int(input())
#     a.append(n)

# sum = sum(a)  # for total
# sum = sum*100/(100*num)

# allsub = []  # for each subject
# for x in range(len(a)):
#     temp = (a[x]*100)/100
#     allsub.append(temp)

# for x in range(len(a)):
#     print("The percentage of the ", x, "subject is:\n", allsub[x])

# print("\n The total percentage is :", round(sum, 2), "%")


# Userin = input("Enter your username: ")
# if(len(Userin) <= 10):
#     print("This is a valid username")
# elif(len(Userin) == 3):
#     print("Are you for real")
# else:
#     print("Too long for username")

# text = input("Enter your comments\n")
# a = ["make a lot of money", "buy now", "click this"]
# spam = False

# for x in range(len(a)):
#     if(a[x] in text):
#         spam = True
#         break
#     else:
#         spam = False

# if(spam):
#     print("Your comment has a spam message")
# else:
#     print("Your comment is being posted")

# comments = input(f"who are you?\n")  # formatting strings with 'f'
# list = ["dad", "mom", "brother", "sister", "relative"]
# check = False
# for x in range(len(comments)):

#     if(list[x] in comments):
#         check = True
#         break
#     else:
#         check = False
# if(check):
#     print("You can enter:")
# else:
#     print("You Unknown identity")


# --------------------------------------


# LOOPS


# n = int(input("Enter The Number"))
# for x in range(1, 11):
#     print(n, "X", x, "=", n*x, "\n")

# l1 = ["Hair", "Eyes", "Brain", "Blood", "Brain tumor"]
# for x in range(len(l1)):
#     if(l1[x][0] == 'E'):
#         print("Greet", l1[x], "\n")

# x = 1
# while x <= 10:
#     print(n, "X", x, "=", n*x, "\n")
#     x += 1

# if(n % 2 == 0):
#     print("Not Prime")
# else:
#     print("Prime")

# li = []
# x = 1
# while x <= n:
#     li.append(x)
#     x += 1
# sum = sum(li)
# print(sum)

# fact = 1
# for x in range(1, n+1):
#     fact = fact*x
# print("Factorial is :", fact)


# for x in range(1, n):
# /// |-
# /// |--
#     for y in range(x):
#         print("x", end=' ')
#     print()

# for x in range(n):
# /// |--
# /// |-
#    for y in range(x, n):
#         print("x", end=' ')
#     print()


# --------------------------------------


# Functions and Recursions


# def func(a, b, c):
#     if(a > b) and (a > c):#important
#         max = a
#     elif(b > c):
#         max = b
#     else:
#         max = c
#     return max

# print(func(11, 12, 1))


# def convo(a):
#     if a[1] in ['f', 'F']:  # NEW
#         celc = (int(a[0]) - 32) * 5/9
#         print(celc)
#     elif a[1] in ['c', 'C']:
#         fahr = (int(a[0]) * 9/5) + 32
#         print(fahr)

# b = []
# # Input for one line
# b = input('Enter your value with degree eg: 123 F -').split()
# convo(b)


# --------------------------------------


# Recursion


# m = int(input("number of terms you want to see "))
# FAB WITH REC
# def rec(n):
#     if n == 0:  # if number entered is zero
#         return 0
#     elif n in [1, 2]:
#         return 1
#     else:
#         return rec(n-1)+rec(n-2)

# print(rec(m)) FOR PRINTING THE DIRECT ANS
# for i in range(m):
#    print(rec(i), end=' ,')  #keep on passing and print answer from 1 to mth value

# SUM OF NUMBERS
# def sum(num):
#     if num <= 1:
#         return num
#     else:
#         return num+sum(num-1)
# print(sum(m))
