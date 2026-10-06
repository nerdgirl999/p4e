
def computepay(h, r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = (r * 40) + ((h - 40) * (r * 1.5))
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(float(hrs), float(rate))

print("Pay", p)