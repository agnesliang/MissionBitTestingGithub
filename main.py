#Create an intro message for the user and come up a good name.
#1) Names: MAp & Cheese
#2) Introduction
print ("\n................Map & cheese.......................")
print("Welcome to Map & Cheese! Been around since '21")
print("Visit our website -> www.mapandcheese.com")
print("our business hours are at the bottom of oru page!")
print ("...................................................\n")

#We want to ask the user for their first & last name 
    #1) Come up with a name - Names:Map & Cheese
first_name = input("Enter your first name:") #Agnes
last_name = input("Enter your last name:") #Liang
age = int(input("Enter your age:")) 
print(f"Full Name: {first_name} {last_name}") #Agnes Liang
correct_name = input("Is your name entered correctly?")#Yes or no

if correct_name != 'yes':
    first_name = input("Enter your first name:") 
    last_name = input("Enter your last name:")
    print(f"Updated Full Name: {first_name} {last_name}")

age = int(input("Enter your age:")) 
print(f"Age: {age}")
correct_age = input("Did you enter your age correctly?")
if correct_age != 'yes':
    age = int(input("Enter your age: "))
    print(f"Updated Age: {age}")
    
# We want to ask the user for their phone number

phone_number = input ("Please put your phone number:")

 
# We want to ask the user if they want takeout or delivery

#We want to ask what cuisine they want

# We want to ask the user for their current address

