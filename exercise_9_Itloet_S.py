username = input("Username: ")
password = input("Password: ")
while username != "admin" or password != "1234":
    print("PLEASE CHECK YOUR USERNAME AND PASSWORD")
    username = input("Username: ")
    password = input("Password: ")
print("LOG IN SUCCESSFUL")
