def vatCal():
    price = int(input("Actual price: "))
    totalprice = price * (1.07)
    return totalprice
print(vatCal())
