# Ask user for their name
name = input("What's your name?").strip().title()

#Splits user name into first name and last name

first, last = name.split(" ")

#Print Format strings
print(f"Hello, {first}")




