from datetime import date
bdate = int(input("Enter Birth Day:"))
bmonth = int(input("Enter Birth Month:"))
byear = int(input("Enter Birth Year:"))

bday = date(byear, bmonth, bdate )
today = date.today()

count_days =  (today - bday).days
count_months = (count_days % 365) // 30
count_years= count_days // 365
 
print(f"You are approximately {count_years} years and {count_months} months old!")