#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
age=input("Enter your age:")
if(int(age)>=18):
    print("You are old enough to learn to drive")
else:
    print(f"wait for the {18-int(age)} more years to learn to drive.")

'''Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
to get the age as input. You can use a nested condition to print
'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
'''

my_age=27
u_age=int(input("Enter your age:"))
if(my_age<u_age):
    print(f"You're {u_age-my_age}years older than me")
elif(my_age==u_age):
    print("We are of same age")
else:
    print(f"You're {my_age-u_age} years younger than me")

#nested form for the same code
my_age=27
u_age=int(input("Enter your age:"))
if(my_age<u_age):
    difference=u_age-my_age

    if(difference==1):
        print("you're are one year older than me")
    else:
        print(f"you're are {difference}years older than me ")

elif(my_age==u_age):
    print("we are of same age")

else:
    difference=my_age-u_age

    if(difference==1):
            print("you're are one year younger than me")
    else:
            print(f"you're are {difference}years youner than me ")
'''
#Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. 
'''
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if(a>b):
     print("a is greater than b")
elif(a<b):
     print("a is smaller than b")
else:
     print("a is equal to b")

'''Write a code which gives grade to students according to theirs scores:

90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''

score=int(input("Enter the score:"))
if(score>=90):
     print("You have passed with A grade")
elif(score >=80 and score<=89):
     print("You have passed with B grade")
elif(score >=70 and score<=79):
     print("You have passed with C grade")
elif(score >=60 and score<=69):
     print("You have passed with D grade")
else:
     print("You have failed")

'''Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
 If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. March, April or May, 
the season is Spring June, July or August, the season is Summer'''

month=input("Enter the Month:")
match month:
    case "September" | "October" | "November":
          print("The season is Autumn")     
    case "December"|"January"|"February":
          print("The season is Winter")
    case "June"|"July"|"August":
          print("The season is Summer")

'''

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
 If the fruit exists print('That fruit already exist in the list')'''

fruits_list=['banana', 'orange', 'mango', 'lemon']
fruit=input("Enter the fruit name you want to add to the list:")
if(fruit in fruits_list):
      print("The fruit name already in the list")
else:
      fruits_list.append(fruit)
      print(fruits_list)


      
