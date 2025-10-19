# This is a car/mortgage loan calculator
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
def time_choice(user):
    if user.lower() == 'y':
        return float(input('\nPlease enter loan duration in years\n')) * 12
    if user.lower() == 'm':
        return float(input('\nPlease enter loan duration in months\n'))
    print('You entered an incorrect character!')
    return time_choice(
        input(
            "\nIf you would like to use years for the term of the loan"
            "enter y, to give the term in months enter m.\n"
        )
    )
def loan_calculator():
    print("\nHello this is a Loan/Mortgage Calculator\n")
    loan_amount = input(
        "\nPlease enter the amount of the loan you wish to calculate.\n"
    )
    while not is_float(loan_amount):
        print("Your entry was incorrect")
        loan_amount = input(
            "\nPlease enter the amount of the loan you wish to calculate.\n"
        )
    loan_amount = float(loan_amount)
    apr = input(
        '\nPlease enter the interest rate.'
        'Enter the number representing the percent. Example 6 for 6%\n'
        )
    while not is_float(apr):
        print('Your entry was incorrect!\n')
        apr = input(
            'Enter a number representing the percent. Example 6 for 6%\n'
        )
    apr = float(apr) / 100
    time = input(
        '\nIf you would like to use years for the term of the loan enter y,'
        'to give the term in months enter m\n'
        )
    loan_duration = time_choice(time)
    monthly_rate = apr / 12
    if loan_duration == 0:
        monthly_payment = loan_amount
    elif apr < .001:
        monthly_payment = loan_amount / loan_duration
    else:
        monthly_payment = loan_amount * (
            monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration))
        )
    print(f"\nWhen taking out a ${loan_amount: ,.2f} dollar loan with a "
          f"{apr * 100: .1f}% interest rate for {int(loan_duration)} months, "
          f"your monthly payments will be; "
          f"${round(monthly_payment, 2): ,} dollars\n"
    )

loan_calculator()