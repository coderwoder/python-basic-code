n = int(input("Enter The Number"))
# /// |--
# /// |-
# for x in range(1, n):
#     for y in range(x):
#         print("x", end=' ')
#     print()

# /// |--
# /// |-
# for x in range(n):
#    for y in range(x, n):
#         print("x", end=' ')
#     print()

# for x in range(1, n):
#     for y in range(x):
#         print("x", end=' ')
#     print()
# for x in range(n):
#     for y in range(x, n):
#         print("x", end=' ')
#     print()

# for x in range(0, n):
#     for y in range(x, n):
#         print(" ", end=' ')
#     for k in range(x+1):
#         print("*", end=' ')
#     print()

# for x in range(0, n):
#     for y in range(x+1):
#         print(" ", end=' ')
#     for k in range(x, n):
#         print("*", end=' ')
#     print()

# for x in range(0, n):
#     for y in range(x+1):
#         print(" ", end=' ')
#     for y in range(x, n-1):
#         print("*", end=' ')
#     for y in range(x, n):
#         print("*", end=' ')
#     print()
# for x in range(0, n):
#     for y in range(x, n):
#         print(" ", end=' ')
#     for y in range(x):
#         print("*", end=' ')
#     for y in range(x+1):
#         print("*", end=' ')
#     print()

for x in range(0, n-1):
    for y in range(x, n):
        print(" ", end=' ')
    for y in range(x):
        print("*", end=' ')
    for y in range(x+1):
        print("*", end=' ')
    print()
for x in range(0, n):
    for y in range(x+1):
        print(" ", end=' ')
    for y in range(x, n-1):
        print("*", end=' ')
    for y in range(x, n):
        print("*", end=' ')
    print()
