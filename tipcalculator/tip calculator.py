print("Welcome to the tip calculator!")
total = float(input("What is your total bill? $\n"))
tip = int(input("How much tip percent would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip_amount = (total) * (tip / 100)

total_amount = round((total + tip_amount) / people , 2)


print(f"Each person should pay: ${total_amount}.")