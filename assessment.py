def load_data(file_data):
    file = open(file_data, "r")
    users_info = file.readlines()

    list_users = []
    for user_info in users_info:
        list_user_info = user_info.split(",")
        list_users.append({
            'username': list_user_info[0],
            'password': list_user_info[1],
            'full name': list_user_info[2],
            'balance': list_user_info[3]
            })
    
    file.close()

    return list_users

def login(username, password):
    for user in list_users:
        if user['username'] == username and user['password'] == password:
            return user
    return

def display_user_information(list_users):
    username = input("Enter Name: ")
    password = input("Enter password: ")
    user_dict = login(username, password)
    if user_dict:
        print("Name: " + user_dict['full name'])
        print("Balance:", float(user_dict['balance']))
    else:
        print("User name and password not found")

    def deposit(username, password, amount):
        for user in list_users:
            if user['username'] == username and user['password'] == password:
                user['balance'] = float(user['balance']) + float(amount)
                print("New balance:", user['balance'])

    def withdraw(username, password, amount):
        for user in list_users:
            if user['username'] == username and user['password'] == password:
                if amount > user['balance']:
                    print("Error! amount is bigger than balance")
                else:
                    user['balance'] = float(user['balance']) - float(amount)
                    print("New balance:", user['balance'])

    def transfer(username, password, amount, user_to_transfer):
        for user in list_users:
            if user['username'] == username and user['password'] == password:
                # print("amount: ",amount)
                # print("user['balance]:", user['balance'])
                if float(amount) > float(user['balance']):
                    print("Error! amount is bigger than balance")
                else:
                    for recipient in list_users:
                        if recipient['username'] == user_to_transfer:
                            user['balance'] = float(user['balance']) - float(amount)
                            recipient['balance'] = float(recipient['balance']) + float(amount)
                            print("New balance:", float(user['balance']))
                            print("recipient balance:", recipient['balance'])
        
    option = input("Do you wish to make a Deposit (select d), a Withdrawl (w), a Transfer (t), or none (n): ")
    option = option.lower()
    if option == 'd':
        amount = input("Input amount to deposit: ")
        deposit(username, password, amount)
    elif option == 'w':
        amount = input("Input amount to withdraw: ")
        withdraw(username, password, amount)
    elif option == 't':
        amount = input("Input amount to transfer: ")
        user_to_transfer = input("Input username to transfer to: ")
        transfer(username, password, amount, user_to_transfer)
    else:
        pass

list_users = load_data("data.txt")
display_user_information(list_users)