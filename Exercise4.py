
# get the username and password from the user.

username = input("Enter your username ")
password = input("Enter your password ")

# check the username and password either correct or wrong.

if username == "admin" and password == "12345":
    print("Login successfull.")
else:
    print("Login failed.")