Part 1: Function 
1.	Write a function named “Greetings” that takes user’s name and print greeting.
Output:       Welcome to SMIT training center, Ahsan 

def greetings (name):
    print("Welcom to SMIT training center",name)


greetings("Ahsan")
    

2.Write a function that takes a number as argument and check if a given number is positive, negative or zero.

def checking (num):
    if num > 0:
        print("positive")

    elif num < 0:
        print("negative")
    else:
        print("Zero")


checking(4)
checking(0)
checking(-2)

3.Write a function to take two numbers as arguments and return the larger number.

def calculate(num1,num2):
    if num1 > num2:
        return (num1)
    else:
        return (num2)

larger_number = calculate(3,9)
print(larger_number)

4.Write a function to take three numbers as argument and return the largest number.

def calculate (num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return ("largest number is: " ,  num1)
    elif num2 > num1 and num2 > num3:
        return ("largest number is:",  num2)
    else:
        return ("largest number is:" ,num3)

largest_num = calculate (20,400,90)
print (largest_num)

5.Write a function to take user’s age as argument and return the message from the function whether he is minor, adult or senior citizen:
a.Minor age is less than 18.
b.Adult age is greater than 18 and less than 60
c.Senior citizen age is greater than 60


def search_age( age):
    if age < 18:
        return("your age is minor ")
    elif age > 18 and age < 60:
        return ("your age is adult")
    else:
        return ("senior citizen")

num = int (input("Enter your age: "))
call = search_age (num)
print(call)

6. Write a function to take integer as argument and check if it is even or odd.

def check_num (num1):
    if num1 %2 == 0:
        return ("This number is even:" , num1)
    else:
        return ("odd:", num1)

check_it = check_num (299)
print(check_it)


7.Write a function to take number as argument and return the square of that number.


def mult (num):
    return num ** 2

check_call = mult (20)
print (check_call)

8.Write a function to compute the area and circumference of the circle and return the computed results.

def compute_circle (num):
    pi = 3.1416
    area = pi * num * num
    circumference = 2 * pi * num
    return (area, circumference)

result = compute_circle (33)

print(result )

9.Write a function to take user’s score as argument and determine if they pass or fail (pass if score is above 60, otherwise fails.)


def result (number):
    if number >=60 :
        return ("you are pass")
    else:
        return ("sorry you are fail")
number = int (input("Enter your score"))
result_call = result (number)
print(result_call)


10.Write a function that evaluates if an input number is prime.

def calculate (num):
    if num % 2 != 0:
        return ("This number is prime: ",num)
    else:
        return ("This number is not prime" , num)

    
num = int (input("Enter a number"))
check_num = calculate (num)
print(check_num)


11.Write a function to compute factorial of a given number using recursion technique.


def fact(num):
    if (num == 1  or num == 0):
         return 1
    return fact(num-1) * num

print(fact(5))

## Part-2: Data Structures (List)
 1.Create a list to store student data i.e. name, age, course and is_attending.
Display each element of list using for loop.
 List = [“Tahir”, 44, “AI and Data Science”, True]

list = ["Tahir","44", "AI Data Science", True]

for i in list :
    print(i)


2.Write a code to separate strings, numbers and Boolean data
from the above listinto separate lists.

lis = ["Tahir",44, "AI Data Science", True]

strings = []
numbers = []
boolean = []

for i in lis:
    if type(i) == str:
        strings.append(i)
    elif type(i) == int:
        numbers.append(i)
    elif type(i) == bool:
        boolean.append(i)
        
    
print("strings : " ,strings )
print("numbers : " ,numbers )
print("boolean : " ,boolean )

3.Create a list [“apple”, “raspberry”, “pineapple”, “cherry”]. 
a.How can you check if apple is present in the list and
get the index of the element (if present)
b.Now replace the raspberry and pineapple with orange.
c.Insert “apricot” at index 2.
d.Extend the resulting list with items “car”, “bike”, “aeroplane”.

list = ["apple", "raspberry", "pineapple", "cherry"]

for i in list:
    if i == "apple":
        print(" apple is found: " ,"index is:" ,list.index("apple"))


list[1:3] = ["orange"]
print(list)


list.insert(1,"apricot")
print(list)

list.extend(["car", "bike", "aeroplane"])
print(list)

4.Write a code to get first and second best scores from the list:
Scores_list = [40, 89, 90, 89, 23, 90, 50]

Scores_list = set([40, 89, 90, 89, 23, 90, 50])

first = max(Scores_list)
Scores_list.remove(first)
second = max(Scores_list)

print("First best score :" ,first )
print("Second best score :", second )


5.Create a list [32,54,66,11,77,10,90]
a.Remove items from the list with values less than 20.
b.Sort the list in ascending and descending order.
c.Now, compute the average value of the list items.

list = [32,54,66,11,77,10,90]

for i in list:
    if i < 20 :
        list.remove(i)

print(list)

list = [32,54,66,11,77,10,90]

list.sort()
print(list)

list.reverse()
print(list)

list = [32,54,66,11,77,10,90]

average = sum(list) / len(list)
print(average)

Gadgets = [“Mobile”, “Laptop”, 10.0, “Marker”, 3, 10, “Speakers”, “Camera”, 310.25]
a.Create separate list of string and numbers,
b.Sort the string list in ascending and descending order
c.Sort the string list by length of elements in the list
d.Sort the numbers list in ascending and descending order

Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

string = []
numbers = []

for i in Gadgets:
    if type (i) == str :
        string.append(i)
    else:
        numbers.append(i)

print("strings list :",string)
print("numbers list :",numbers)


string.sort()
print("ascending order of string list:" , string)

string.reverse()
print("descending order of list:",string)


string.sort(key=len)
print("sort string by length of elements: ",string)

numbers.sort()
print("ascending order :",numbers)

numbers.reverse()
print("descending order: ", numbers)



























               
