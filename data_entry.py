from datetime import datetime

date_format = "%d-%m-%Y"

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
    pass

def get_category():
    pass

def get_description():
    pass