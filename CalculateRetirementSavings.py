from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def calculate_savings():
    return True

# Function to validete if the date has the correct format
def validate_date(date_in):
    try:
        date_out=datetime.strptime(date_in, '%Y-%m-%d')
    except ValueError:
        return False
    return True
# Function to validate if value if negative or equals to 0
def validate_number_values(number_in):
    if number_in < 0:
        return False
    return True

def main():
    date_of_birth=''
    monthly_saving=0
    percent_interest_generated=0
    monthly_capitalize=False

    # Input and validate if entry is in correct format
    date_of_birth=input('Enter your birthdate(in the format yyyy-mm-dd): ')
    while not validate_date(date_of_birth):
        date_of_birth=input('Date Format error: Re-enter your birthdate(in the format yyyy-mm-dd, i.e: 1990-08-25): ')
    print(date_of_birth)
    monthly_saving=input('Enter your monthly salary: ')
    while not validate_number_values(monthly_saving):
        monthly_saving=input('Ingresed value is negative: Re-enter your monthly salary: ')
    print(monthly_saving)
    percent_interest_generated=input('Enter the interest rate that savings will generate: ')
    while not validate_number_values(percent_interest_generated):
        percent_interest_generated=input('Ingresed value is negative: Re-enter the interest rate that savings will generate: ')
    print(percent_interest_generated)
    # while monthly_capitalize:
    #     percent_interest_generated
    # calculate_savings(date_of_birth,monthly_saving,percent_interest_generated)

if __name__=='__main__':
    main()