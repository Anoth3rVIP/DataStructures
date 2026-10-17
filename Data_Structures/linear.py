found = False
numbers = [1,2,34,70,8,5,23,6,87,40,7,34,77,42,97,4,53,202,2304,55,3]
target = int(input('Enter the targer number: '))

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index "+str(i))
        found = True
        break
if found == False:
    print("Element not found")