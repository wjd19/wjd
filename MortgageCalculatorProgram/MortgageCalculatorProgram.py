
# Mortage calculator

#retrieve home value, down payment, and principal
home_value = round(float(input("How much is the home worth?\n")), 2)
down_payment = round(float(input("\nHow much are you paying for the down payment?\n")), 2)
principal = home_value - down_payment
answer = input(f"\nGreat. So that means the principal of the loan is {principal}, right?\n").lower().strip()

#make sure 0f principal value of loan
if answer == "no":
    principal = float(input("\nOh, ok. What is the principal amount?\n"))
else:
    print("\nAwesome.\n")

#get more key info for calculations -- going to assume user has a fixed rate mortgage
loan_rate = float(input("\nWhat is your yearly mortgage interest rate?\n")) / 100
monthly_loan_rate = loan_rate / 12
loan_length = float(input("\nHow many years until your loan must be paid off in full?\n"))
num_monthly_payments = 12 * loan_length

paranth = (1 + monthly_loan_rate) ** num_monthly_payments
distr = monthly_loan_rate * paranth
distr2 = principal * distr
fixed_rate_payments = round((distr2 / (paranth - 1)), 2)

print(f"\nFor your ${int(home_value)} home, you're making a down payment of ${int(down_payment)} \
and taking on a {loan_length} year loan at a fixed annual rate of {round(loan_rate * 100, 2)}%.")

print(f"\nThis means you'll need to pay ${fixed_rate_payments} per month for your mortgage before \
property taxes and other fees.")

answer = input("\nIf you would like your total monthly payment \
calculation to include property taxes and HOA fees, type 'yes'.\n").lower().strip()

property_taxes = 0
hoa_fees = 0

if answer == "yes":
    property_taxes = round(float(input("\nEnter your monthly property tax amount:\n")), 2)
    print('')
    hoa_fees = round(float(input("Enter your monthly HOA fees:\n")), 2)
    total_monthly_payment = round(fixed_rate_payments + hoa_fees + property_taxes, 2)

    print(f"\nYour total monthly payment -- including mortgage, HOA fees, and property taxes --\
 is ${total_monthly_payment}.\n")

    print("\nThank you for using our mortgage calculator. Have a great day.")

else:
    print("\nSince there is nothing else, thank you for using our mortgage calculator. Have a great day.")
