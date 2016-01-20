hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rate = raw_input("Enter Rate:")
rate = float(rate)
if hrs <= 40.0:
    print hrs*rate
else:
    print ((40.0*rate)+((hrs-40.0)*(rate*1.5)))
