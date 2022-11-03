#function in program
def login():
    username = input("PLEASE INPUT USERNAME: ")
    password = input("PLEASE INPUT PASSWORD: ")
    if username == "admin" and password == "1234":
        return True
    else: return False
def showmenu():
    print("-----welcome to TigerframAlpha-----")
    print("MENU")
    print("1. VAT calculator")
    print("2. PRICE calculator")
def menuselect():
    selectmenu = int(input(">>"))
    if selectmenu == 1:
        print(vatcal())
    else: print(totalprice())
def vatcal():
    actual_price = int(input("Product price: "))
    result = actual_price * 1.07
    return "Total price is " + str(result)
def totalprice():
    price_1 = int(input("First product price: "))
    price_2 = int(input("Second product price: "))
    return "Total price is " + str((price_1 + price_2) * 1.07)

#gathering the function
def my_shop():
    if login() is True:
        showmenu()
        menuselect()
        return "--THANK YOU--"
    else: return "-----CAN'T LOGIN-----"
print(my_shop())
