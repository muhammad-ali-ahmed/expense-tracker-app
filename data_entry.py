from datetime import datetime

date_format = "%d-%m-%Y"

CATEGORY = {"I":"Income", "E":"Expense"}

def get_date(prompt, allow_default=False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return valid_date.strftime(date_format)
    
    except ValueError:
        print("Invalid Date Format! Please Enter the date in dd-mm-yy format ")
        return get_date(prompt, allow_default)
    

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <=0 :
            raise ValueError("Amount must be in non-negative non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for income or 'E' for Expense): ").upper()
    if category in CATEGORY :
        return CATEGORY[category]
    else:
        print ("Invalid category!")
        return get_category()
    
    
    

def get_description():
    return input("Enter description (optional): ")