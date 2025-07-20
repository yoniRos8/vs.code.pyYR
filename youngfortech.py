

#empty_list=[]

# blabla=["banana","1",True,"banana",52.444]
# blabla.remove("banana")
# print(blabla)
# blabla.insert(2,"bla")
# print(blabla)


# list=[1,2,3,4,5,6]
# sumHezka=0
# for item in list:
#     if item%2==0:
#         sumHezka+=item*item
# #print (sumHezka)


# for i in range(5):
#     print(i)


# import random
# x=random.randint(1,100)

# guess=int(input("Enter your guess: "))
# attempts=1
# while guess != x:
#     if(guess<x):
#         print("Too low, Try again!")
#     elif(guess>x):
#         print("Too high, Try again!")
#     guess=int(input("Enter new guess: "))
#     attempts+=1

# print("Your right!!!!, the number is",x)


# def from_celsius_to_fahrenheit(num):
#     return int(num)*float(9/5)+32

# def from_fahrenheit_to_celsius(num):
#     return (int(num)-32)*float(5/9)

# choice=input("Wich conversion would you like to perform?" \
# "1:Celsius to Fahrenheit" \
# "2:Fahrenheit to Celsius ")

# if(choice=="1"):
#     num=input("Enter the temperature in Celsius: ")
#     x=from_celsius_to_fahrenheit(num)
#     print(num,"°C IS",x,"°F")
# else:
#     num=input("Enter the temperature in Fahrenheit: ")
#     x=from_fahrenheit_to_celsius(num)
#     print(num,"°F IS",x,"°C")



# my_list=["apple","banana","cherry"]
# my_list.append(["date","elderberry"])
# print(my_list)

# for i in range(1,7):
#     if(i%3==0):
#         print(i*2)



#משימות תכנות חובה:
#תרגיל 1:

def find_max(numbers):
    max_num=numbers[0]
    for item in numbers:
        if(item>max_num):
            max_num=item
    return max_num
numbers=[3,5,2,8,1,9,4]
print(find_max(numbers))

#תרגיל 2

def even_numbers(arr):
    even_arr=[]
    for num in arr:
        if(num%2==0):
            even_arr.append(num)
    return even_arr
 
  
original_list=[1,4,5,7,8,10,13]
print(even_numbers(original_list))


#תרגיל 3
def isuporder_sorted(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return False
    return True
test_list=[1,2,3,4,5]
print(isuporder_sorted(test_list))

#תרגיל 4
def reverse_code(str):
    return str[::-1]

str="!hello,world"
print(reverse_code(str))

#תרגיל 5
def cuount_aeiou (str):
    count=0
    for i in range(len(str)):
        if(str[i]=="a" or str[i]=="u" or str[i]=="e" or str[i]=="i" or str[i]=="o"):
            count+=1
    return count

str2="hi, my name is yoni"
print(cuount_aeiou(str2))

#בונוסים

def is_prime(num):
    if(num<2):
        return False
    for i in range(2,10):
        if(num%i==0 and i!=num):
            return False
    return True

def find_primenum(x,y):#x ,y -הטווח
    for i in range(x,y+1):
        if(is_prime(i)):
            print(i)

find_primenum(1,100)


def is_palindrom(str):
    revstr=reverse_code(str)
    for i in range(len(str)):
        if(str[i]!=revstr[i]):
            return False 
    return True

print(is_palindrom("iyooyi"))


def longest_world(str):
    current=" "
    longest=" "
    for i in range(len(str)):
        if(str[i]!=" "):
            current+=str[i]
        else:
            if(len(current)>len(longest)):
                longest=current
            current = ""
                
    if(len(current)>len(longest)):
        longest=current
    return longest


print(longest_world("hi my name is yonatan"))
        


def find_longest_word(arr):
    newarr=[]
    max1=0
    maxword=""
    
    for fruit in arr:
        if(len(fruit)>max1):
            max1=len(fruit)
            maxword=fruit

    for fruit in arr:
        if(fruit==maxword):
            newarr.append(fruit)
    return newarr

words_list=["apple","banana","orange","strawberry","kiwi","pineapple"]
print(find_longest_word(words_list))


def find_palindromes(arr):
    newarr=[]
    for item in arr:
        if(is_palindrom(item)):
            newarr.append(item)
    return newarr

words_list=["radar","apple","level","banana","stats","noon"]
print(find_palindromes(words_list))

