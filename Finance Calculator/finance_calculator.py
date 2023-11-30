#This code calculates the return on investements and home loan.

import math

print("investment - to calculate the amount of interest you'll earn on your investment.\nbond - to calculate the amount you'll have to pay on a home loan.")


calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Making sure the user's input is not user sensitive.
calculation.lower()

# Making sure the calculation type is entered the right way
if calculation != "bond" and calculation != "investment":
    print("You entered an invalid input. Please try again.")
    calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    calculation.lower()


if calculation == "investment":
    deposit = float(input("Enter the amount you want to deposit: "))
    rate = float(input("Enter the interest rate: "))/100
    years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Enter S for simple interest or C for compound interest: ")

    if interest == 'S':
        A = round((deposit * (1 + rate*years)), 2)
    else:
        A = round((deposit *math.pow((1 + rate), years)), 2)
    
    print(f"Your money after interest is R{A}")

elif calculation == "bond":
    house_value = float(input("Enter your house value: "))
    rate = float(input("Enter the interest rate:"))/100
    months = float(input("Enter the number of months you plan to repay the bond: "))
    repayment = round(((rate*house_value)/(1-(1+rate)**(-months))), 2)
    print(f"You will have to repay R{repayment} each month.")