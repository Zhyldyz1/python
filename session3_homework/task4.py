# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!

# sec_password = "Python123"
# while True:
#     user_pass = input("Please enter your password: ")
#     if user_pass == sec_password:
#         print("Access Granted!")
#         break  
#     else:
#         print("Wrong password. Please try again.")
tpl = (1, 2, True, 10.10, "Hello", 1)
print(tpl)
print(type(tpl))
print(tpl[-2])