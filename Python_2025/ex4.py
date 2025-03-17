# Prompts the user to enter an age
age = int(input("Please enter your age: "))

# Judge by age and output the corresponding discount information
if age <= 19:
    print("You are eligible for a student discount.")
elif 20 <= age <= 54:
    print("You are not eligible for any age discount.")
else:  # age >= 55
    print("You can enjoy senior discount.")
