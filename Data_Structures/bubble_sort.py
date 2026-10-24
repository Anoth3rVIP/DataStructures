list = [20,2,4,5,2,40,5,13,28,53,24,35,37]

# n = len(list)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
# print(list)

n = len(list)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)