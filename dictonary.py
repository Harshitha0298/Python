# Create an empty dictionary called dog
dog={}
# Add name, color, breed, legs, age to the dog dictionary
dog={"name":"tommy","colour":"brown","breed":"golden retriver","legs":4,"age":4}
print(dog)
print(dog.values())
# Create a student dictionary and add first_name, first_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary
student={"first_name":"Adya","last_name":"Shastri","gender":"Women","age":20,"marital_status":"Single","skills":["python","sql","GCP"],"country":"India","city":"davangere","address":"Ns layout"}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("java")
student["skills"].extend(["html","css"])
print(student)
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
print(student.pop("skills"))
print(student)
# Delete one of the dictionaries
del dog
print(dog)
