def is_armstrong(num):
    digits = str (num)
    power = len(digits)
    total = sum (int(d)**power for d in digits)
    return total == num
print (is_armstrong(153))

def armstrong_in_range(start,end):
    return [num for num in range (start,end) if is_armstrong(num)]

print (armstrong_in_range(1,1000))