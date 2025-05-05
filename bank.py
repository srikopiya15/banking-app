account={}
next_account_number=10000
next_customer_id=1
    
def empty(filename):
    try:
        file=open(filename,"r")
        data=file.read().strip()
        file.close()
        return data ==""
    except:
        return True

def admin_signup():
    print("\n---Admin Sign-Up---")
    username=input("Create admin username:")
    password=input("Create admin password:")
    file=open("admin.txt","w")
    file.write(username +"\n"+ password)
    file.close()
    print("Admin registered successfully.\n")

def admin_login():
    print("\n---Admin login---")
    try:
        file=open("admin.txt","r")
        lines=file.readlines()
        file.close()
        if len(lines)< 2:
            print("Admin credetials not found.")
            return False
        saved_user=lines[0].strip()
        saved_pass=lines[1].strip()
        username=input("Create admin username:")
        password=input("Create admin password:")
        if username==saved_user and password==saved_pass:
            print("login successful!\n")
            return True
        else:
            print("invalid credentials.")
            return False
        except:
            print("Error reading admin file.")
            return False

def generate_account_number():
    global next_account_number
    account=str(next_account_number)
    next_account_number +=1
    return account

def generate_customer_id():
    global next_customer_id
    cus_id="CUSTOMER"+ str(next_customer_id)
    next_customer_id+=1
    return cus_id

def create_account():
    name=input("enter account holder name:")
    balance("enter  initial balance:")
    if not is_valid_number(balance):
        print("invalid balance.")
        return
    account_no=generate_account_number
    cus_id=generate_customer_id
    accounts[account_no]={
        'customer_id':cus_id,
        'name':name,
        'balance':float(balance)
        'transaction':[f"Account created with balance{balance}"]
    }
    print("Account created successfully.")
    print("Account number:",account_no)
    print("Customer ID:"cus_id)
    account_file(account_no,accounts[account_no])

def deposit
    account=input("Enter Account Number:")
    if account not in accounts:
        print("Account not found.")
        return
    amount=input("Enter amount to deposit:")
    if not is_valid_number(amount):
        print("invalid amount.")
        return
    amounts=float(amount)


