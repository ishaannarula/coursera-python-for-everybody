hrs = input('Please enter number of hours worked.')
rate_per_hr = input('Please enter your hourly wage.')

hrs_float = float(hrs)
rate_per_hr_float = float(rate_per_hr)

def computepay(hrs_float, rate_per_hr_float) :
    if hrs_float <= 40 :
        return hrs_float * rate_per_hr_float
    else :
        return 40 * rate_per_hr_float + (hrs_float - 40) * rate_per_hr_float * 1.5

print('Pay', computepay(hrs_float, rate_per_hr_float))
