from datetime import datetime
# from dateutil.relativedelta import relativedelta

def age_checker(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise Exception("Incorrect format, format required YYYY-mm-dd")
    
    