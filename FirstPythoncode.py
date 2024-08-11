# A simple Python script for beginners

# 1. Variables
name = "Alice"  # A variable to store a string
age = 30        # A variable to store an integer

# 2. Print a greeting message
print("Hello, " + name + "!")
print("You are " + str(age) + " years old.")

# 3. Conditionals
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# 4. Loops
print("\nCounting from 1 to 5:")
for i in range(1, 6):  # Loop from 1 to 5
    print(i)

# 5. Functions
def greet_person(person_name):
    """This function greets a person with their name."""
    return "Hello, " + person_name + "!"

# Using the function
greeting_message = greet_person("Bob")
print("\n" + greeting_message)

# 6. User Input
user_name = input("What's your name? ")
user_age = int(input("How old are you? "))

print("\nHello, " + user_name + "!")
print("You are " + str(user_age) + " years old.")

# Conditionals with user input
if user_age < 18:
    print("You are a minor.")
elif user_age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
