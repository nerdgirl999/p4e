largest = None
smallest = None
total = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        ival = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival

    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival

    num = ival + 1
    total = total + ival

print("Maximum", largest)
print("Minimum", smallest)