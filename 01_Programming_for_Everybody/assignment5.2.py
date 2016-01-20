largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    try:
        if num == "done" : break
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest