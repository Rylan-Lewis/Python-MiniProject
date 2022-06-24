# Check = "^[a-z][A-Z][0-9][@&%]"
import re
PASSWORD=input("Input your password")
def check(x):
    while True:
        if (len(x)<5 or len(x)>10):
            break
        elif not re.search("[0-9]",x):
            break
        elif not re.search("[a-z]",x):
            break
        elif not re.search("[@&%]",x):
            break
        elif not re.search("[A-Z]",x):
            break
        elif re.search("\s",x):
            break
        else:
            print("Valid Password")
            break
    if False:
        print("Not a valid Password")
print(check(PASSWORD))
