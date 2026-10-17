numbers = [2,5,10,46,500,678,24536,30000,868643,68977464]

target = int(input("Enter target number: "))
low = 0
high = len(numbers)-1
found = False
while low <= high:
    mid = (low +high) // 2
    if numbers[mid] == target:
        print("Element found at index: ", mid)
        found = True
        break
    elif target < numbers[mid]:
        high = mid - 1
    else: low = mid +1
if not found:
    print("Element not found!")