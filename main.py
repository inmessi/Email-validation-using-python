
import re

email_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"

email = input("Enter your email: ")

if re.search(email_cond, email):
    print ("Right Email")
else:
    print ("Wrong Email")
