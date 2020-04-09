import logging

logging.basicConfig(level=logging.INFO)

def calculate_savings():
    return True

# Function to validete if the date has the correct format
# def validate_date(date_in):
#     try:
#         date_out=datetime.strptime(date_in, '%Y-%m-%d')
#     except ValueError:
#         return False
#     return True
# Function to validate if value if negative or equals to 0
def validate_number_values(number_in):
    if number_in < 0:
        return False
    return True

def main():
    starting_age = 0
    monthly_saving = 0
    percent_interest_generated = -1
    monthly_capitalize = False

    # Input and validate if entry is in correct format
    while starting_age<=0:
        starting_age=int(input('Enter the age that you started to save money (i.e: 25): '))
    print(starting_age)
    while monthly_saving<=0:
        monthly_saving=float(input('Enter your monthly amount of the money that you save: '))
    print(monthly_saving)
    while percent_interest_generated<0:
        percent_interest_generated=float(input('Enter the interest rate that savings will generate (i.e: 3.54, it can be 0 if any interest is generated): '))
    print(percent_interest_generated)
    # while monthly_capitalize:
    #     percent_interest_generated
    # calculate_savings(starting_age,monthly_saving,percent_interest_generated)

if __name__=='__main__':
    main()