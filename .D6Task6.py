# list the even number and odd number

list1 = [10,501,22,37,100,999,87,351]
Even_list = []
Odd_list = []

for num in list1:
    if num%2 == 0:
        Even_list.append(num)
    else:
        Odd_list.append(num)

print(Even_list)
print(Odd_list)

#count the prime number in the list

list2 = [10,501,22,37,100,999,87,351]
count = 0
for num in list2:
    if num == 0 or num == 1:
        continue
    for i in range(2, num//2 + 1):
        if num%i == 0:
            break
    else:
        count += 1
print(count)    


