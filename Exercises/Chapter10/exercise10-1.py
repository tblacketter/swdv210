def main():
    
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()

    email = get_email()
    print()

    phone = get_phoneNumber()
    print()
    formattedPhoneNumber = format_phoneNumber(phone)

    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.") 
    print(f"We'll text your confirmation code to this number: {formattedPhoneNumber}")            
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
def get_email():
    while True:
        atSymbol = False
        dotCom = False

        email = input("Enter your email:        ").strip()
        print()

        if email.find("@") != -1:
            atSymbol = True
        
        suffix = email[(len(email))-4:]
        if suffix == ".com":
            dotCom = True

        if atSymbol == True and dotCom == True:
            return email
        else:
            print("Your email must contain an @ sign and must be succeeded with \'.com\'") 
   
def get_phoneNumber():
    while True:
        phone = input("Please enter your phone number: ").strip()

        phone.replace(".", "")
        phone.replace(" ", "")
        phone.replace("-", "")
        phone.replace("(", "")
        phone.replace(")", "")

        if len(phone) != 10:
            print("Phone number must be 10 digits only")
        else:
            if phone.isdigit() == True:
                return phone
            else:
                print("Phone number must contain only numerical digits")    

def format_phoneNumber(phone):
    prefix = phone[0:3]
    middle = phone[3:6]
    suffix = phone[6:]

    tempList = [prefix, middle, suffix]
    formattedPhone = ".".join(tempList)
    return formattedPhone


if __name__ == "__main__":
    main()