# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
total=0
for x in courses.values():
    total=total+x
print(total)
percentage=(total*100)/500
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corrina Cortes':66,'Peter Wrden':75}
max_marks_scored=max(mathematics.values())
for i in mathematics:
    if mathematics[i]==max_marks_scored:
        topper=i
        print("Topper:",topper)
        break;
print("Maximum marks:",max_marks_scored)
# Code ends here 


# --------------
# Given string
topper = 'andrew ng'
# Code starts here
name=topper.split()
first_name=name[0]
last_name=name[1]
full_name=last_name+" "+first_name
certificate_name=full_name.upper()
print("Certificate Name:",certificate_name)
# Code ends here


