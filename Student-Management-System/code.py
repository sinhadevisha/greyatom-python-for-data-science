# --------------
# Code starts here
# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print("New Class: ", new_class, end='\n')
# Append the list
new_class.append('Peter Warden')
# Print updated list
print("After Adding Peter: ", new_class, end='\n')
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print("After Removing Carla: ", new_class, end='\n')
# Create the Dictionary for Geoffrey Hinton
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print("Marks Obtained by Geoffrey Hinton: ", courses, end='\n')
# Slice the dict and stores  the all subjects marks in variable
math = courses['Math']
english = courses['English']
history = courses['History']
french = courses['French']
science = courses['Science']
# Store the all the subject in one variable `Total`
total=0
for x in courses.values() : total = total + x
# Print the total
print("Total Marks of Geoffrey Hinton: ", total, end='\n')
# Insert percentage formula
percentage = ( total * 100 ) / 500
# Print the percentage
print("Percentage of Geoffrey Hinton: ", percentage, end='\n')
# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corrina Cortes':66,'Peter Wrden':75}
# Given string
max_marks_scored = max(mathematics.values())
print ("Maximum Marks in Mathematics: ", max_marks_scored, end='\n')
# topper = list(mathematics.keys())[list(mathematics.values()).index(max_marks_scored)]
topper = max(mathematics, key = mathematics.get)
print("Topper in Mathematics: ", topper, end='\n')
# Create variable first_name 
first_name = topper.split()[0]
# Create variable Last_name and store last two element in the list
last_name = topper.split()[-1]
# Concatenate the string
full_name = last_name + " " + first_name
# print the full_name
print("Full Name of Topper: ", full_name, end='\n')
# print the name in upper case
certificate_name = full_name.upper()
print("Certificate Name of Topper: ", certificate_name, end='\n')
# Code ends here


