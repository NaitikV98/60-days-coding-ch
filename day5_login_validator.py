correct_username = "admin"
correct_password = "12345"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Invalid username or password.")

        if attempts < 3:
            print("Attempts remaining:", 3 - attempts)
        else:
            print("Too many failed attempts. Login blocked.")