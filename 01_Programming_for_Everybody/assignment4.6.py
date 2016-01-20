def computepay(h,r):
    if hrs <= 40.0:
        return hrs*rate
    else:
        return ((40.0*rate)+((hrs-40.0)*(rate*1.5)))


hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate"))
p = computepay(hrs,rate)
print p