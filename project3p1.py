hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
overtimeRate = r * 1.5
pay = 40 * r

if h > 40:
    overtime = h - 40
    oPay = overtimeRate * overtime + pay
    print ("Pay: ", oPay)
    print("Overtime hours worked: ", overtime)
else:
    print("Pay: ", pay)
