import os

accounts={}
next_account_number=10000
next_customer_id=1


def is_file_empty(filename):
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

def generate_account_number():
    global next_account_number
    accounts=str(next_account_number)
    next_account_number +=1
    return accounts

def generate_customer_id():
    global next_customer_id
    cus_id="CUSTOMER"+ str(next_customer_id)
    next_customer_id+=1
    return cus_id

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
        'transaction':[]
    }
    print("Account created successfully.")
    print("Account number:",account_no)
    print("Customer ID:",cus_id)

    save_user_credentials(cus_id,username,password)

    append_account_to_file(account_no,accounts[account_no])

def save_user_credentials(cus_id,username,password):
    try:
        with open("user_credentials.txt","a") as file:
            file.write(f"{cus_id}|{username}|{password}\n")
    except:
        print("error writing user credentials to file")

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
    if "transaction" not in accounts[account]:
        accounts[account_no]["transaction"]=[]
    accounts[account]['transaction'].append(f"deposited{amounts}")
    print("deposit successfully.")

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
    accounts[account]['transaction'].append(f"withdrew{amount}")
    print("withdrawal successfully.")

def check_balance():
    account=input("enter account number:")
    if account in accounts:
        print("corrent balance:",accounts[account]['balance'])
    else:
        print("account not found.")

def transaction_history():
    account=input("enter account number:")
    if account in accounts:
        print("transaction history")
        for t in accounts[account]['transaction']:
            print("-",t)
    else:
        print("account not fount")


def customer_info():
    account=input("enter account number:")
    if account in accounts:
        info=accounts[account]
        print("\n---Customer Info---")
        print("account number:",account)
        print("customer ID:",info['customer_id'])
        print("name:",info['name'])
        print("balance:",info['balance'])
        print("transaction:")
        for t in info['transaction']:
            print("-",t)
    else:
        print("account not found.")
def append_account_to_file(account_no,info):
    try:
        file=open("bank_data.txt","a")
        line=account_no +"|"+info['customer_id']+"|"+info['name']+"|"+str(info['balance'])+"|"+",".join(info['transactions'])+"\n"
        file.write(line+"\n")
        file.close()
    except:
        print("successfully writing file.")

def save_all_data():
    try:
        file=open("bank_data.txt","w")
        for account_no,info in accounts.items():
             line=account_no +"|"+info['customer_id']+"|"+info['name']+"|"+str(info['balance'])+"|"+",".join(info['transaction'])+"\n"
        file.write(line)
        file.close()
    except:
        print("error saving data.")

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
menu()
            






