#string concatination

first_name="Harshitha"
last_name="chilla"
print("full_name=",first_name+' '+last_name)

#escape char
a=5
print("my name is Harshitha\nI am doing python challenge")
print('I want to print \"hello world\"')

#replace
price = "$1345,69"
print(price.replace(",",".").replace("$",""))

number="123-456-984"
print(number.replace("-",""))

number = '+46 (176) 574-8987'
print(number.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ",""))

#f string
name="Harshitha"
age=27
married=True
print("My name is "+name+" and I am "+str(age)+"years old and Married"+str(married)) #old method
print(f"My name is {name} and I am {age} years old and Marital status {married}") #f string method

#split
Timeframe='2026-06-24 23:30:00'
print(Timeframe.split(" "))
print(Timeframe.split("-"))

csv="123,Mark,USA,27"
print(csv.split(","))

#indexing
text="python" 
print(text[5])
print(text[-1])

#slicing
date="2026-08-02"

#extract year
print(date[0:4])
print(date[:4])

#extract month
print(date[5:7])

#extract date
print(date[8:])

#whitespacecleanup
text=" Engineering"
print(text.lstrip())

text="Engineering   "
print(text.rstrip())

text=" Engineering "
print(text.strip())

text="###Data##"
print(text.strip("#"))

#upper and lower
data="email"
search="Email "
print(data.upper())
print(search.lower())

print(data.lower().strip()==search.lower().strip())

#messy data to clean data
data="968-maria,(D@t@ Engineer );;27y  "
print(data.replace("968-","").replace(","," ").replace("(","").replace("@","a").replace(")","").replace(";","").strip())

#search
phone="+46 945-3453"
print(phone.startswith("+46"))

email="abc@gmail.com"
print(email.endswith(".com"))
print("@" in email)

phone1="+46-123-4567"
phone2="48-475-3847"
phone3="0046-483-0493"
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

#validation
country="India"
print(country.isalpha())
num="28399"
print(num.isnumeric())


#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print("Thirty","Days","of","Python")

'''Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().P'''

company="Coding "+"For "+"All"
print(company)
#print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company[0:7])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.lower().find("coding"))
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"))

#Split the string 'Coding For All' using space as the separator (split()) 
value="Coding For All"
print(value.split(" "))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
value="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(value.split(","))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
w1="Python"
w2="For"
w3="Everyone"
print("acronym=",w1[0]+w2[0]+w3[0])

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find("C"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentance='You cannot end a sentence with because because because is a conjunction'
print(sentance.find("because"))
print(sentance.index("because"))
print(sentance.rfind("because"))
print(sentance.rindex("because"))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentance[sentance.find("because"):sentance.rfind("because")+len("because")])

#Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
#Does 'Coding For All' end with a substring coding?
print(company.endswith("Coding"))

#   Coding For All      '  , remove the left and right trailing spaces in the given string.
string='  Coding For All      '
print(string.strip())

'''Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python'''
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
library=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(library))

'''Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.'''
print("I am enjoying this challenge.\nI just wonder what is next.")

'''Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki'''
print("Name\t Age \t Country \t City \nAsabeneh \t25 \tFinland \tHelsinki")

'''Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.'''
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
a=8
b=6
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")
print(f"{a}//{b}={a//b}")
print(f"{a}**{b}={a**b}")
