hrs = input('Please enter hours worked')
rate_per_hr = input('Please enter rate per hour')

hrs_float = float(hrs)
rate_per_hr_float = float(rate_per_hr)

if hrs_float <= 40 :
    pay = hrs_float * rate_per_hr_float
else :
#    pay = hrs_float * rate_per_hr_float * 1.5
    pay = 40 * rate_per_hr_float + (hrs_float - 40) * rate_per_hr_float * 1.5

print(pay)
