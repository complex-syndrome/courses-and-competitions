import validators as v

if v.email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")
