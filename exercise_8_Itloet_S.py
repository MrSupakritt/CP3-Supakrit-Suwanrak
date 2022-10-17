print("HELLO USER!")
id = input("Username: ")
password = input("Password: ")
if id == "user" and password == "python":
    print("done!")
    print("-------WELCOME TO TIGER SHOP-------")
    print("MENU")
    keyboard = 3950
    mouse = 2490
    bundle = 6000
    print("1. Keyboard ", keyboard, "BAHT")
    print("2. Mouse    ", mouse, "BAHT")
    print("3. Bundle   ", bundle, "BAHT")
    basket = input("What do you want today?: ")
    if basket == "keyboard" or basket == "Keyboard":
        amount = int(input("How many do you want?: "))
        confirm = input("Type 'YES' to confirm your order:")
        if confirm == "YES":
            print("TOTAL:", keyboard * amount, "Baht")
        else:
            print("ORDER CANCELED")
    elif basket == "Mouse" or basket == "mouse":
        amount = int(input("How many do you want?: "))
        confirm = input("Type 'YES' to confirm your order:")
        if confirm == "YES":
            print("TOTAL:", mouse * amount, "Baht")
            print("THANK YOU")
        else:
            print("ORDER CANCELED")
    elif basket == "bundle" or basket == "Bundle":
        amount = int(input("How many do you want?: "))
        confirm = input("Type 'YES' to confirm your order:")
        if confirm == "YES":
            print("TOTAL:", bundle * amount, "Baht")
        else:
            print("ORDER CANCELED")
    else:
        print("WAIT FOR UPDATE")
else:
    print("--please check your Username and Password--")
