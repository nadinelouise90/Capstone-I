# The user inputs their choice of finance calculator, choosing from the menu of 'investment' or 'bond'.
# The program outputs the relevant question prompts to the user based upon the input (using if-elif-else statements) to collect further data.

import math

# Using colour text output to the console for a clearer user experience. Green for user action. White for information. Red for error.

GREEN = '\033[92m'  
LIGHTRED = '\033[91m'
WHITE = '\033[0m'

print("╔══════════════════════════════════════════════════════════════════════════════════╗")
print("                         FINANCE CALCULATOR OPTIONS MENU")
print("  investment - to calculate the amount of interest you'll earn on your investment")
print("  bond - to calculate the amount you'll have to pay on a home loan")
print("╚══════════════════════════════════════════════════════════════════════════════════╝")

menu_choice = input(f"{GREEN}Enter either 'investment' or 'bond' from the menu above to proceed: ")
print("\n")

# User chooses interest finance calculator by inputting 'investment'.
# User is prompted for values required for investment calculations. Numerical values have been cast to a float data type to account for any fractions of number.

if menu_choice.lower() == "investment":
    deposit_amount = float(input("How much money are you depositing in £? "))
    interest_rate = float(input("What is the interest rate as a percentage? "))
    years_to_invest = float(input("How many years do you plan on investing for? "))
    interest = input("Do you want simple or compound interest? ")
    converted_int_rate = interest_rate/100

    # If-else statements are used to determine whether the program should calculate simple interest or compound interest based upon the previous inputs.
    # Below is the logic for calculating simple interest.

    if interest.lower() == "simple":
        total_amount = deposit_amount * (1 + (converted_int_rate*years_to_invest))
        format_total_amount = "{:.2f}".format(total_amount)
        print(f"{WHITE}╔══════════════════════════════════════════════════════════════════════════════════╗")
        print(f"        After {years_to_invest} years at an interest rate of {interest_rate}%, you will get back £{format_total_amount}")
        print("\n")
        print("    Initial deposit:           £{:.2f}".format(deposit_amount))    #Formatting the string to display monetary values to 2 decimal places.
        print(f"    Interest rate:             {interest_rate}%")
        print(f"    Duration of investment:    {years_to_invest} years")
        print("    Profit:                    £{:.2f}".format(total_amount-deposit_amount))
        print(f"    Total return:              £{format_total_amount}")
        print("\n")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝")

    # Below is the logic for calculating compound interest.
    else:
        total_amount = deposit_amount * math.pow((1+converted_int_rate), years_to_invest)
        format_total_amount = "{:.2f}".format(total_amount)
        print(f"{WHITE}╔═══════════════════════════════════════════════════════════════════════════════════╗")
        print(f"        After {int(years_to_invest)} years at an interest rate of {interest_rate}%, you will get back £{format_total_amount}")
        print("\n")
        print("    Initial deposit:           £{:.2f}".format(deposit_amount))
        print(f"    Interest rate:             {interest_rate}%")
        print(f"    Duration of investment:    {years_to_invest} years")
        print("    Profit:                    £{:.2f}".format(total_amount-deposit_amount))
        print(f"    Total return:              £{format_total_amount}")
        print("\n")
        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

# User chooses bond finance calculator by inputting 'bond'       

elif menu_choice.lower() == "bond":
    house_value = float(input("What is the current value of the house? "))
    interest_rate = float(input("What is the interest rate as a percentage? "))
    months = int(input("How many months do you plan to take to repay the bond? ")) # We don't expect fractions of a month here so int() is used.

    monthly_int_rate = (interest_rate/100)/12
    repayment = (monthly_int_rate*house_value)/(1- (1+monthly_int_rate)**(-months))
    formatted_repayment = "{:.2f}".format(repayment)

    print(f"{WHITE}╔═══════════════════════════════════════════════════════════════╗")
    print(f"        Your monthly repayments will be £{formatted_repayment}")
    print("\n")
    print("         House Value:               £{:.2f}".format(house_value))
    print(f"         Interest rate:             {interest_rate}%")
    print(f"         Repayment Term:            {months} months")
    print(f"         Monthly repayment:         £{formatted_repayment}")
    print("\n")
    print("╚═══════════════════════════════════════════════════════════════╝")


else:
    print(f"{LIGHTRED}You have not inputted a valid option. Please type either 'interest' or 'bond'.")

