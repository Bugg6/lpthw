from sys import argv

script, first, third = argv

print("Here is your script", script)
print("Here is your first variable", first)
second = input("Please enter a second variable: ")

print(f"Here is the input variable {second}, and here is your last variable: {third}")
