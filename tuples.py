# Create an empty tuple
my_tuple=()
print(my_tuple)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_sis=("saanch",'lakshi','danu','khushi')
my_bro=("hrishi",'vinu','rohi')

# Join brothers and sisters tuples and assign it to siblings
my_siblings=(my_sis+my_bro)
print(my_siblings)
# How many siblings do you have?
print(len(my_siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members=list(my_siblings)
family_members.extend(['jyothi','ganesh'])
print(family_members)

# Unpack siblings and parents from family_members
*sibling,mother,father=family_members
print(sibling)
print(mother)
print(father)

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('apple','mango','banana')
vegetables=('potato','tomato','onion')
animal_products=("panner","milk","chiken")
food_stuff_tp=(fruits+vegetables+animal_products)
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=food_stuff_tp
print(food_stuff_lt)

# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
# Delete the food_stuff_tp tuple completely
del food_stuff_lt

# Check if an item exists in tuple:
#print(food_stuff_lt)

# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
