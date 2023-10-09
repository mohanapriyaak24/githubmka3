# 1. list the even number and odd number

list1 = [10,501,22,37,100,999,87,351]
Even_list = []
Odd_list = []

for num in list1:
    if num%2 == 0:
        Even_list.append(num)
    else:
        Odd_list.append(num)

print("Even Number List : ",Even_list)
print("Odd Number List :  ",Odd_list ,"\n")

# 2. count the prime number in the list

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
print("PrimeNumber count in the List: ", count, "\n")  


# 4. print sum first and last digit of the number

def addFirstAndLast(n):
    num = str(n)
    First_num = int(num[0])
    Last_num = int(num[-1])
    sum = First_num + Last_num
    print("sum of first and last digit in the number: ", sum, "\n")
addFirstAndLast(4567)


# 6. the duplicates  in the list


def findDup(list):
    l1=[]
    DupList = []   
    for i in list:
        if i not in l1:
            l1.append(i)
        else:
            DupList.append(i)
    print("Duplicates in this list: " ,DupList ,"\n")

list1 = [1,2,2,3,3,3,4,4,5,7,7,]
list2 = [4,67,67,99,90,90,6,64]
list3 = [23.89,78,6,7,7,9,9,4,4,6,9]

findDup(list1)
findDup(list2)
findDup(list3)

# 7. first non-repeating element in the list

list1= [2,3,4,2,3,5,6]
l1= []
for i in list1:
     if list1.count(i) == 1:
         l1.append(i)
         
print("First non-repeating element in the list : ",l1[0],"\n")
        

# 8. find the minimum element in the rated and sorted list

list1 = [10,501,22,37,100,999,87,351]
list1.sort()
print("Minimum element in the sorted list: ",list1[0],"\n")

# 9. Find the triplets in the list whose sum is equal to 59

def findTriplets(list1, sum ,lenL):

    for i in range(lenL-2):

        for j in range(i+1,lenL-1):
            
            for k in range(j+1,lenL):
                if list1[i]+list1[j]+list1[k] == sum:
                    print("Triplets in this list: ",list1[i],list1[j],list1[k],"sum is:",sum)
                    return True
            
    return False
    
list1 = [10 ,20,30,9]
sum = 59
lenL =len(list1) 
findTriplets(list1,sum,lenL)

# 10. print sub-list of sum is zero

def subList(list1,len2):

    for i in range(len2):
        sum = list1[i]
        if sum == 0:
            return True
        for j in range(i+1,len2):
            sum += list1[j]
            return True
        return False
    
list1 = [4,2,-3,1,6]
len2 = len(list1)

if subList(list1,len2)==True:
    print("Yes ,There is a sub-list with sum zero")
else:
    print("No sub-list with sum zero")


subList(list1,len2)







