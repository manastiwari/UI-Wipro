largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        x = int(num)
    except:
        print("Invalid input")
    if num == "done" : break
    largest = -1
    for n in [x]:
        if n>largest:
            largest = n
    for n in [x]:
        if smallest is None:
            smallest = n
        elif n<smallest:
            smallest = n

print("Maximum", largest)
print("Minimum", smallest)
