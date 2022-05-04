
# Mortage calculator

#take in user input for dollar value of home as well as interest rate
#make sure to account for variable/fixed interest rate type
#mortgage length in years

#begin program
home_value = float(input("How much is the home worth? "))
down_payment = float(input("How much are you paying for the down payment? "))
principal = home_value - down_payment
answer = input(f"Great. So that means the principal of the loan is {principal}, right?")
answer = answer.lower()
answer = answer.strip()

if answer == "no":
    principal = float(input("Oh, ok. What is the principal amount? "))
else:
    print("Awesome.")

loan_rate = float(input("What is your yearly mortgage interest rate? ")) / 100
monthly_loan_rate = loan_rate / 12
loan_type = input(f"Is your loan type fixed or variable? Please enter 'fixed' or 'variable'. ")
loan_type = loan_type.lower().strip()
loan_length = float(input("How many years until your loan must be paid off in full? "))
num_monthly_payments = 12 * loan_length

print(f"Home value: {home_value}")
print(f"Loan rate: {loan_rate}")
print(f"monthly_loan_rate: {monthly_loan_rate}")
print(f"Loan Type: {loan_type}")
print(f"Loan length: {loan_length}")
print(f"num_monthly_payments: {num_monthly_payments}")

paranth = (1 + monthly_loan_rate) ** num_monthly_payments
distr = monthly_loan_rate * paranth
distr2 = principal * distr
divide = round((distr2 / (paranth - 1)), 2)
print(divide)







