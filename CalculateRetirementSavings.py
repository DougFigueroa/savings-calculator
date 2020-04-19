import logging

logging.basicConfig(level=logging.INFO)

def calculate_savings(age,retire_age,amount,interest,m_capitalize):
    years_saving=(retire_age-age)
    months_saving=years_saving*12
    savings = 0
    if m_capitalize:
        interest_cap = interest/12
        for i in range(1, months_saving+1):
            savings = (savings+amount)*(1+(interest_cap/100))
    else:
        anual_amount=amount*12
        for i in range(1, years_saving+1):
            savings = (savings+anual_amount)*(1+(interest/100))
    
    return savings

# Function to validete if the date has the correct format DEPRECATED
# def validate_date(date_in):
#     try:
#         date_out=datetime.strptime(date_in, '%Y-%m-%d')
#     except ValueError:
#         return False
#     return True
# Function to validate if value if negative or equals to 0
def main():
    starting_age = 0
    monthly_saving = 0
    percent_interest_generated = -1
    monthly_capitalize = False
    retirement_age = 60

    # Input and validate if entry is in correct format
    while starting_age <= 0:
        starting_age = int(input('Enter the age that you started to save money (i.e: 25): '))
    print(starting_age)
    while monthly_saving <= 0:
        monthly_saving = float(input('Enter your monthly amount of the money that you save: '))
    print(monthly_saving)
    while percent_interest_generated < 0:
        percent_interest_generated = float(input('Enter the interest rate that savings will generate (i.e: 3.54, it can be 0 if any interest is generated): '))
    print(percent_interest_generated)
    if percent_interest_generated > 0:
        monthly_capitalize = True if str(input('The savings are monthly capitalize? (type Y: yes and N: no if the savings are annually capitalize): ')).upper()=='Y' else False
        print(monthly_capitalize)
    result = calculate_savings(starting_age,retirement_age,monthly_saving,percent_interest_generated,monthly_capitalize)
    print('The savings at age of '+str(retirement_age)+' will be: \n')
    print(result)

if __name__=='__main__':
    main()