
#Phase 1: Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back
# into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
size_lim = 42
zander_len = float(input("Input the length of the zander: "))
if zander_len < size_lim:
    below_lim = size_lim - zander_len
    print("A zander must be 42 centimeters or longer")
    print("This fish is smaller than the size limit", below_lim, "cm")
    print("It must be returned to the lake")
else:
    print("This fish meets the size allowance. Congrats!")

# Phase 2: Write a program that asks the user to enter the cabin class of a cruise ship and then prints out
# a written description according to the list below. You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class
cabinClass = input("Enter the cabin class (LUX, A, B, C): ")
if cabinClass == "LUX":
    print("Upper-deck cabin with a balcony")
elif cabinClass == "A":
    print("Above the car deck, equipped with a window")
elif cabinClass == "B":
    print("Windowless cabin above the car deck")
elif cabinClass == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class !!!")

# Phase 3: Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender = input("Are you male of female? ")
hemoValue = float(input("Input your hemoglobin value (g/l): "))
if gender == "male":
    if hemoValue < 134:
        print("Your hemoglobin value is low")
    elif hemoValue > 167:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")
else:
    if hemoValue < 117:
        print("Your hemoglobin value is low")
    elif hemoValue > 155:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")

# Phase 4: Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")