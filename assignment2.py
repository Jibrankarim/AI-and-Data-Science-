## Q1.Write a program that checks if a given number is positive, negative or zero. 
##num = int (input("Enter number to find negative, positive and zero: "))

if num > 0:
    print("The Number is positive.")
elif num < 0:
    print ("The Number is negative.")
else:
    print("The Number is Zero")


## Q2. Write a program to find the larger of the two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(" The first number is larger then", num2)
elif num2 > num1:
    print("The second number is larger then", num1)
else:
     print("both are numbers are equal.")

## Q3. Write a program to find the largest of the three numbers.

num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))
num3 = int (input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print ("first number is largest: " , num1)
elif num2 >= num1 and num2 >= num3:
    print ("second number is largest number" , num2)
else:
    print("third number is largest number" , num3)


##Q4. Write a program to check if the given string “Mass” is present in the string “Saylani Mass IT”.
##If the string is present then display the message “string found”.

text = "Saylani Mass IT"

if "Mass" in text:
    print("string found")
else:
    print (" string not founf")

## Q5. Write a program to take user’s age as input and display whether he is minor, adult or senior citizen:
 a. Minor age is less than 18.
 b. Adult age is greater than 18 and less than 60
 c. Senior citizen age is greater than 60

num = int (input ("Enter your age : "))

if num <= 18 :
    print ("you are minor")

elif num > 18 and num <= 60:
    print("you are adult")
else:
    print("you are senoir citizen")

## Q6. Write a program to take integer as input and check if it is even or odd.

num = int (input ("Enter a number"))

if num % 2 == 0:
    print("this number is even: ",num)
else:
    print("this number is odd")

## Q7.Write a program to take two numbers and an operator (/,x,+,-)
## as input and perform the corresponding operation. 


num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))
operator = (input("Enter any operator( -, +, *, /):  "))

if operator == "/" :
    result = num1 / num2

elif operator == "-" :
    result = num1 - num2

elif operator == "+" :
    result = num1 - num2

elif operator == "*" :
    result = num1 - num2

else:
    print("something wrong")


print("Result: ", result)

##Q8. Write a program to take number as input and check if it lies in the range i.e.
20(inclusive) – 40 (exclusive)


num = int (input("Enter a number: "))

if num >= 20 and num < 40:
    print ("yes your number is between 20 and 40 range")
else:
    print("your number is out of this range")


##Q.9 Write a program that ask for an integer number and checks if it is divisible by 2, 3, or both.

num = int(input("Enter a number "))

if num % 2  == 0 and num % 3  == 0:
          print("your number is divisible for both 2 and 3")
elif num % 2  ==0 :
    print ("your number is divisible for only 2: ")
elif num  % 3  == 0:
    print ("your number is divisible for only 3")
else:
    print("your number is not divisible for both")


##Q.10 Write a program to take user’s score as input and determine if they pass or fail (pass if score is above 60, otherwise fails.)

num = int (input("Enter your score: " ))

if num >= 60 :
    print("your are pass")
else:
    print ("sorry Fail")

##Q.11 Write a program that evaluates if an input number is prime

num = int (input("enter any number: "))

if num % num == 0:
       print("your input number is not  prime")
else:
    print("your number is  prime")

##Q.12 Write a program that takes a temperature in Celsius and checks if it is freezing, moderate or hot.
##a. Freezing temperature is below 0.
##b. Moderate temperature is greater than 0 and less than 26.
##c. Hot temperature is above 26.

tem = float (input ("enter temperature is celsius: "))

if tem < 0:
    print (" temperature is freezing")

elif tem > 0 and tem <= 26:
    print(" temperature is moderate")

elif tem > 26 :
    print("temperature is hot")

else:
    print("wrong input")


##Part-2: Loops

##Q.1 Write a program to print numbers from 1 to 30 using for loop.

for i in range (1 , 31):
    print (i)


##Q.2 Write a program to print even numbers from 1 to 50 using while loop

i = 1
while i <= 50:
    if i%2 ==0:
        print(i)
    i+=1



##Q.3 Write a program to print multiplication table of a given number.

num = int (input("enter number: "))

i = 1
while i <= 10:
    print(num * i)
    i+=1

##Q.4 Write a program to print odd numbers from 1 to 50 using while loop

i = 1
while i <= 50:
    if i%2 != 0:
        print(i)
    i+=1


##Q.5 Write a program to calculate the sum of all numbers from 1 to 50 using for loop

sum = 0
   
for i in range(1, 51):
    sum += i
   
print("the sum of numbers from 1 to 50 is:",sum)
    


##Q 6 Write a program to print each character of a string.

text = "JIBRAN KARIM"

for i in text:
    print(i)

##Q.7 Write a program to compute the factorial of a number using while loop

num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1

print("factorial :", fact)

num = 5
fact = 1
for i in range (1, num+1):
    fact *= i

print("fact",fact)

##Q.8 Write a program to print numbers from 10 down to 1.
[Hint: first check the sequence generated by range function on IDLE using this command
i.e. list(range(10, 0, -1))]


for i in range(10, 0, -1):
    print(i)


##Q.9 Write a program that continues to ask user to input password until the correct password is entered.

user_password = input("enter your pasword")
correct_password = "JIBran.123"

if user_password == correct_password :
    print("your passowrd is correct")
else:
    print("wrong password")

##Q.10 Write a program to print the square of each number from 1 to 10 using for loop.

for num in range (1, 11):
    square =  num * num
    print (f"squre of {num} is {square}")



##Q. 11 Write a program to calculate the sum of even and odd numbers and print them. (numbers from 1 to 50)

even_num = 0
odd_num = 0

for i in range (1, 51):
    if i %2 == 0:
        even_num += i
    else:
        odd_num += i

print(f"{even_num} {odd_num}")


##Q.12 Bonus Challenge: Write a program to print the first 10 Fibonacci numbers
using for loop. Hint:
First 10 Fibanacci numbers are  0,1,1,2,3,5,8,13,21,34

num1 = 0
num2 = 1
num3 = 10

for i in range (num3):
    print(num1)

    num4 = num1 + num2
    num1 = num2
    num2 = num4
   



























































































           



           




























    





























































