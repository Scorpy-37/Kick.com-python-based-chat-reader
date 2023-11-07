from os import system

def find_closest_string(lst, target):
    highest_similarity = 0
    closest_string = ""
    for string in lst:
        similarity = 0
        for char in str.lower(target):
            if char in str.lower(string):
                similarity += 1
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_string = string
    return closest_string

print("What do you want to do?\n1: Install\n2: Repair\n3: Uninstall")
choice = input("> ")
closest = find_closest_string(["1: Install", "2: Repair", "3: Uninstall"], choice)
if closest == "1: Install":
	system("pip install selenium==4.10.0")
	system("pip install undetected_chromedriver")
	input("Successfully installed all required packages!")
elif closest == "2: Repair":
	system("pip uninstall undetected_chromedriver")
	system("pip uninstall selenium")
	system("pip install selenium==4.10.0")
	system("pip install undetected_chromedriver")
	input("Successfully reinstalled all required packages!")
elif closest == "3: Uninstall":
	if str.lower(input("This is not recommended, are you sure you want to uninstall? (yes)\n> ")) == "yes":
		system("pip uninstall undetected_chromedriver")
		system("pip uninstall selenium")
		input("Successfully uninstalled all required packages!")
else:
	input("Unknown option, please try again")