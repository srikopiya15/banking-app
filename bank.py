import os

accounts={}
next_account_number=10000
next_customer_id=1 

#create empty file
def is_file_empty():
    try:
        with open("admin.txt","r")as file:
            data=file.read().strip()
            return data == ""
    except:
        return True

is_file_empty()

#sign up admin
def admin_signup():
    if os.path.exists("admin.txt"):
        print("Admin already registered.proceeding to login...\n")
        return
    print("\n---Admin Sign-Up---")
    username=input("Create admin username:")
    password=input("Create admin password:")
    with open("admin.txt","w")as file:
        file.write(username +"\n"+ password)
    print("Admin registered successfully.\n")

admin_signup()

#login admin
def admin_login(): 
    while True:
        print("\n---Admin login---")
        try:
            with open("admin.txt","r")as file:
                lines=file.readlines()
            if len(lines)< 2:
                print("Admin credetials not found.")
                return False
            saved_user=lines[0].strip()
            saved_pass=lines[1].strip()
            username=input("enter admin username:")
            password=input("enter admin password:")
            if username==saved_user and password==saved_pass:
                print("login successful!\n")
                return True
            else:
                print("invalid credentials.")
        except FileNotFoundError:
            print("Error reading admin file.")
            return False 
        
#valid number
def is_valid_number(text):
    dot=0
    for c in text:
        if c=='.':
            dot+=1
            if dot>1:
                return False
        elif c <'0'or c > '9':
            return False
    return len(text) > 0

#creat account number
def generate_account_number():
    global next_account_number
    accounts=str(next_account_number)
    next_account_number +=1
    return accounts

#create customer ID
def generate_customer_id():
    global next_customer_id
    cus_id="CUSTOMER"+ str(next_customer_id)
    next_customer_id+=1
    return cus_id

#account creating
def create_account():
    name=input("enter account holder name:")
    address=input("enter address:")
    email=input("enter email address:")
    username=input("create a username:")
    password=input("create a password:")
    balance=input("enter  initial balance:")

    if not is_valid_number(balance):
        print("invalid balance.")
        return
    account_no=generate_account_number()
    cus_id=generate_customer_id()
    accounts[account_no]={
        'customer_id':cus_id,
        'name':name,
        'address':address,
        'email_address':email,
        'username':username,
        'password':password,
        'balance':float(balance),
        'transactions':[]
    }
    print("Account created successfully.")
    print("Account number:",account_no)
    print("Customer ID:",cus_id)

    save_user_credentials(cus_id,username,password)

    append_account_to_file(account_no,accounts[account_no])

#save separate informations
def save_user_credentials(cus_id,username,password):
    try:
        with open("user_credentials.txt","a") as file:
            file.write(f"{cus_id}|{username}|{password}\n")
    except:
        print("error writing user credentials to file")

#amount deposit
def deposit():
    account=input("Enter Account Number:")
    if account not in accounts:
        print("Account not found.")
        return
    amount=input("Enter amount to deposit:")
    if not is_valid_number(amount):
        print("invalid amount.")
        return
    amounts=float(amount)
    accounts[account]['balance']+=amounts
    accounts[account]['transactions'].append(f"deposited{amounts}")
    print("deposit successfully.")

    append_account_to_file(account,accounts[account])

#amount withdraw
def withdraw():
    account=input("enter account number:")
    if account not in accounts:
        print("account not found.")
        return
    amount=input("enter amount to withdraw:")
    if not is_valid_number(amount):
        print("invalid amount")
        return
    amounts=float(amount)
    if amounts>accounts[account]['balance']:
        print("insufficient balance.")
        return
    accounts[account]['balance']-=amounts
    accounts[account]['transactions'].append(f"withdrew{amount}")
    print("withdrawal successfully.")

    append_account_to_file(account,accounts[account])

#balance checking
def check_balance():
    account=input("enter account number:")
    if account in accounts:
        print("corrent balance:",accounts[account]['balance'])
    else:
        print("account not found.")

#transaction history
def transaction_history():
    account=input("enter account number:")
    if account in accounts:
        print("transaction history")
        for t in accounts[account]['transactions']:
            print("-",t)
    else:
        print("account not fount")

#customer information
def customer_info():
    account=input("enter account number:")
    if account in accounts:
        info=accounts[account]
        print("\n---Customer Info---")
        print("account number:",account)
        print("customer ID:",info['customer_id'])
        print("name:",info['name'])
        print("balance:",info['balance'])
        print("transaction:",[])
        for t in info['transactions']:
            print("-",t)
    else:
        print("account not found.")

#writing bank data file
def append_account_to_file(account_no,info):
    try:
        file=open("bank_data.txt","a")
        line=account_no +"|"+info['customer_id']+"|"+info['name']+"|"+str(info['balance'])+"|"+",".join(info['transactions'])+"\n"
        file.write(line+"\n")
        file.close()
    except:
        print("successfully writing file.")
    
#save data in bank data text
def save_all_data():
    try:
        with open("bank_data.txt","w")as file:
            for account_no,info in accounts.items():
                line=account_no +"|"+info['customer_id']+"|"+info['name']+"|"+str(info['balance'])+"|"+",".join(info['transactions'])+"\n"
                file.write(line)
        print("All data saved successfully.")
    except Exception as e:
        print(f"error saving data.{e}")

#load data in bank data text
def load_data():
    global next_account_number,next_customer_id
    try:
        file=open("bank_data.txt","r")
        lines=file.readlines()
        file.close()
        for line in lines:
            parts=line.strip().split("|")
            if len(parts) < 5:
                continue
            account_no=parts[0]
            accounts[account_no]={
                'customer_id':parts[1],
                'name':parts[2],
                'balance':float(parts[3]),
                'transactions':parts[4].split(",")
            }
            if int(account_no) >= next_account_number:
                next_account_number=int(account_no)+1
            num=parts[1].replace("CUSTOMER","")
            if num.isdigit() and int(num)>=next_customer_id:
                next_customer_id=int(num)+1
    except:
        pass

load_data()

#main menu system
def menu():
    while True:
        print("\n---Mini Banking---")
        print("1.Creat Account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Transaction History")
        print("6.Customer Info")
        print("7.Exit")
        choice=input("enter your choice:")
        if choice=="1":
            create_account()
        elif choice=="2":
            deposit()
        elif choice=="3":
            withdraw()
        elif choice=="4":
            check_balance()
        elif choice=="5":
            transaction_history()
        elif choice=="6":
            customer_info()
        elif choice=="7":
            save_all_data()
            print("All data saved. Good Bye!")
            break
        else:
            print("Invalid Choice.")

if admin_login():
    menu()




