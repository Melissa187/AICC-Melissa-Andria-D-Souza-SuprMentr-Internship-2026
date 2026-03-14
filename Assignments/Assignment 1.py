correct_password = "python123"
password = input("Enter password: ")
if len(password) < 6:
    print("Password too short")
elif password == correct_password:
    print("Access granted")
else:
    print("Access denied")
