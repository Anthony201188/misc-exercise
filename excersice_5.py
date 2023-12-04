#excercise for numbers and comparisions.

# --- Task 1 ---
#- Write a program which asks the user for three numbers and prints the sum of those numbers

""" example output 
Example output:

```
$ sh sum.py
Enter number: 200
Enter number: 500
Enter number: 300
Sum of the numbers: 1000
``` 
print()
print("****************")
print("TASK 1")
print()

# define the input variables

num_1 = input( "please write your first number: ")
num_2 = input( "please write your second number: ")
num_3 = input( "please write your third number: ")

#converting the strings into integers using type casting
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

#calculating the sum of the intigers.
sum_of_numbers = num_1 + num_2 + num_3


#print the sum of the numbers
print("sum of the numbers: ", sum_of_numbers )

print()
print("END OF TASK 1")
print("*********************")


# --- Task 2 ---
#- Write a program that asks the user for two numbers
#- If the number1 is greater than number2, print "First number is greater!"
#- If the number2 is greater than number1, print "Second number is greater!"
#- If the number1 is equal to number2, print "Numbers are equal!"
#- If both numbers are greater than 10000, print "Numbers are beeeeeeg!"
print()
print("****************")
print("TASK 2")
print()

#initialising my inputs and notice this time I have vast the type of the input as an intiger all in the same line.
number_1 = int(input("enter your first number here: "))
number_2 = int(input("enter your second number here: "))
number_sum = number_1 + number_2

# using the if condtinional statement to forfull the other part of the task stating condtiions of the entered numbers

if number_1 > number_2:
    print("Your first number is greater than your second number")
    
if number_1 < number_2:
    print("Your second number is greater than your first number")

if number_1 == number_2:
    print("Numbers are equal")

if number_sum > 1000:
    print("Numbers are biiiiiiiig!!!")
        
print()
print("END OF TASK 2")
print("*********************")


# --- Task 3 ---
#- Write a program which asks the user for five numbers and prints the largest of those numbers.

print()
print("****************")
print("TASK 3")
print()

#initialising the input variables although ensuring I use slightly different versions for each tasks, the variables could be re-assinged but i wanted clean varlaibles with no values etc..
# note - a variable is initialised using the = , but can be defined using my_variable: str then later initialised by my_variable = "hello"
num_one = int(input("enter your first number here: "))
num_two = int(input("enter your second number here: "))
num_three = int(input("enter your third number here: "))
num_four = int(input("enter your fourth number here: "))
num_five = int(input("enter your fith number here: "))

#next I will put those varaibles into a list 
list_1 = [num_one, num_two, num_three, num_four, num_five]

#next ill initilaise a largest varialbe using 0 in square brackets this means the first indexed item in the list this will then later be comared against all elements in the list 
largest = list_1[0]

#next I will use a for loop to iterate over those inputs and store the highest in the largest variable from the temporary var used in the loop
for var in list_1:
    if var > largest:
        largest = var

print("The largest number is: ", largest)

print()
print("END OF TASK 3")
print("*********************")





# --- Task 5 ---
#-  write a program which asks the user for a number and prints if it is even and divisible by 3.

print()
print("****************")
print("TASK 5")
print()

#initiaise and type cast the input

example_number = int(input("Enter your number here: "))

# next ill create a function that checks if the number is even by using a modulus operator which chekcs if anything is left over when dividing by 2 ad if so the number is NOT even
def is_even(num): #this defines the function and sets "num" as the empty argument variable
    return num % 2 == 0

#Ill do the same for is it divisible by 3
def is_divisible(num_2): #this defines the function and sets "num_2" as the empty argument variable
    return num_2 % 3 == 0

#next I use the print function with the function to print the results

print("Is your number even? " ,is_even(example_number))
print("Is your number evedivisible by 3? " ,is_divisible(example_number))


print()
print("END OF TASK 5")
print("*********************")

"""

# --- Task 4 ---
#-  Your task is to write a Python program to asks for a month name and prints the number of days in that month.

print()
print("****************")
print("TASK 4")
print()

#for this task ill use a dictionary with numbers of days in each month as the data and the key as the name of the month

dic_1 = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

#next initialise an inpur variable for the user
month = input("Enter the month of the year here starting witha capital letter: " )


# next ill use a for loop to iterate over the dictionary and check them against the inpur variable
for value in dic_1.keys():    # note here the".values" method from dictinaries which is used to detone the right hand info from the : side od the dictionary, there is also a key() method which lets you select the key
    if value == month:        # note that here the variable value is compared to the input
        print("number od days in this month: ", dic_1[value])   # finally here the variable "value" in the loop is then called to print that value from the dictionary using square brackets



print()
print("END OF TASK 5")
print("*********************")        
        
