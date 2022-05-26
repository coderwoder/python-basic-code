# TEST

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

# l1=[1,2,0]
# l1.sort()
# l1.reverse()
# l1.append(2.79)
# l1.insert(0,"Ready")
# l2=len(l1)
# print(l1[:-1])
# l1.pop(2)
# l2=l1.pop(1)
# print(l2)
# l1.remove(0)
# print(l1)


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


# print(list(mynary.keys()))
# print(mynary.values())
# print(mynary.items())
# update01 = {
#     "fast": "but no slow",
#     3: 4,
#     "slow": "hump"
# }
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

# a=[3,1,5,6]
# IF AND ELSE
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
