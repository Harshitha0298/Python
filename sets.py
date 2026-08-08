a={10,30,60,40,70}
a.add(90)
a.update('11','33')
print(a)
a.remove(30)
a.pop()
a.discard(33)

a={10,30,40,60}
b={20,50,40,10}
print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b-a)

print(a.symmetric_difference(b))
print(a^b)

a={20,10}
b={30,40,10,20}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b)) #no common


a={50,80}
b={30,40,10,20}
print(a.isdisjoint(b))

# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['SEB','NORDEA','TCS'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('TCS')
print(it_companies)
# What is the difference between remove and discard
#it_companies.remove('FIS')#It will throw error if trying to deleted the value that don't exist
it_companies.discard('FIS') #It will not throw error if trying to deleted the value that don't exist
print(it_companies)
# Exercises: Level 2
# Join A and B
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.union(b))

# Find A intersection B
print(a.intersection(b))
# Is A subset of B
print(a.issubset(b))
# Are A and B disjoint sets
print(a.isdisjoint(b))
# Join A with B and B with A
print(a.union(b))
print(b.union(a))

# What is the symmetric difference between A and B
print(a.symmetric_difference(b))
# Delete the sets completely
del a 
del b
#print(b)
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
set_age=set(age)
print(len(age)-len(set_age))
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence=("I am a teacher and I love to inspire and teach people.")
word=sentence.split()
print(word)
print(set(word))
