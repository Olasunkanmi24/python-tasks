principal = float(input("enter principal: "))
rate = float(input("enter annual interest rate: "))
monthly_interest_rate = (rate/100)/12
duration = float(input("enter duration: "))
duration_months = duration * 12

mortgage = (principal * monthly_interest_rate  * ((1 + monthly_interest_rate )**duration_months))/ (((1 + monthly_interest_rate )**duration_months) - 1)
print (round(mortgage, 2))
