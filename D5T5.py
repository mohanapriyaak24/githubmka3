# count number of vowels in string

g = "Guvi Geeks Network Private Limited"
count = 0
for i in g:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count+1
print(count)
        
print()


#pyramid program

for i in range(1,21):
    print(" "*(21-i),end =" ")
    for j in range(1,i+1):
        print(j,end=" ")

    print()

print()

#remove vowels from a string

def removevow(string):
    for i in string:
        if i in vowels:
            string = string.replace(i,"")
    print(" vowel Removed from string :",string)
string ="Guvi Geeks Network Private Limited"
vowels ="aeiouAEIOU"

removevow(string)



print()

    
# find its palindrome or not
            
        
def findpalindrome (str1,str2):
    if str1 == str2:
        print("True")
    else:
        print("False")
print("check its palindrome or nor")
str1 = input("Enter a word: ")
str2 = str1[::-1]
findpalindrome( str1,str2)
        
print()

#count no of words in a


def NoOfWords(str):
    space = " "
    count =1
    for i in str:
        if i in space:
            count = count+1
    print("No of Words in a string is : ",count)
str = "find number of word in a string"
NoOfWords(str)

print()

# check its anagram or not

def checkAnagram(str1,str2):
    if str1 == str2:
        print("True")
    else:
        print("False")
print("check if its anagram")

str1 = sorted(input("Enter a word: "))
str2 = sorted(input("Enter a word: "))
checkAnagram(str1,str2)
    
    
