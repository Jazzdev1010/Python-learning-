from datetime import date
bdate = int(input("Enter Birth Day:"))
bmonth = int(input("Enter Birth Month:"))
byear = int(input("Enter Birth Year:"))

#age_in_days = (date.today() - date(birth_year, birth_month, birth_day)).days

bday = date(byear, bmonth, bdate )
today = date.today()

count_days =  (today - bday).days
count_months = (count_days % 365) // 30
count_years= count_days // 365
 
print(f"You are approximately {count_years} years and {count_months} months old!")