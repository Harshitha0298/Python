#Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 
print("fruits",fruits)
print("num of fruits:",len(fruits))
print("vegetables",vegetables)
print("number of vegetables:",len(vegetables))

#Declare an empty list
empty=[]
print(empty)

#Declare a list with more than 7 items
bts=['joon','jin','yoongi','j-hope','jimin','tae','jk']
#Find the length of your list
print(len(bts))

#Get the first item, the middle item and the last item of the list
print(bts[0],bts[-1],bts[(len(bts)//2)])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type=("Maria",27,163,'married','sweden')

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google', 'Microsoft', 'Apple', 'IBM','Oracle','Amazon'] 
#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print("first company:",it_companies[0])
print("middle company",it_companies[len(it_companies)//2])
print("last company",it_companies[-1])

#Print the list after modifying one of the companies

for i, company in enumerate(it_companies):
    if company == 'Amazon':
        it_companies[i] = 'Flipkart'

print(it_companies)

#Add an IT company to it_companies
it_companies.append("TCS")
print(it_companies)
#Insert an IT company in the middle of the companies list
it_companies.insert(4,'SEB')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[it_companies.index('Apple')] = 'Apple'.upper()
print(it_companies)

# Join the it_companies with a string '#;  '
print("# ".join(it_companies))

# Check if a certain company exists in the it_companies list.
print("SEB" in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:4])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies
print(it_companies)

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=(front_end+back_end)
#full_stack=(front_end,back_end)
#front_end.append(back_end)
#print(front_end)
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5,'python')
full_stack.insert(6,'SQL')
print(full_stack)

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("Min age :",min(ages))
print("Max age:",max(ages))
# Add the min age and the max age again to the list
ages.append(min(ages))
print(ages)
ages.append(max(ages))
print(ages)

# Find the average age (sum of all items divided by their number )
print("avg of ages",sum(ages)/2)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third,*scandic = country
print(first)
print(scandic)
