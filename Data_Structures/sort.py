prod_List = []
price_List = []

loop = True
while loop:
    prod_List.append((input("Enter product name: ")))
    price_List.append(int(input("Enter product price: ")))
    loop = False

for i in range(1, len(prod_List)):
    key=prod_List[i]
    j=i-1
    while j >= 0 and prod_List[j] > key:
        prod_List[j+1] = prod_List[j]
        j-=1
    prod_List[j+1] = key
    
for i in range(1, len(price_List)):
    key2=price_List[i]
    j=i-1
    while j >= 0 and price_List[j] > key2:
        price_List[j+1] = price_List[j]
        j-=1
    prod_List[j+1] = key2
print("Products = "+str(prod_List))
print("Prices = "+ str(price_List))

if input("Would you like to add a new product") == "yes" or "Yes":
    loop = True