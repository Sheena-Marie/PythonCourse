# Entering the data
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
#troubleshooting for any idiots
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Numbers, not letters, please!")
    # if this doesn't work, just quit the program
    quit()

#continue on as normal
overtimeRate = r * 1.5
pay = 40 * r

if h > 40:
    overtime = h - 40
    oPay = overtimeRate * overtime + pay
    print ("Pay: ", oPay)
    print("Overtime hours worked: ", overtime)
else:
    print("Pay: ", pay)
