game_library = {
    1: {"name" : "Donkey Kong", "copies": 5, "price": 4},
    2: {"name" : "Super Mario Bros", "copies": 3, "price": 6},
    3: {"name" : "Tetris", "copies": 4, "price": 4},
    4: {"name" : "Minecraft", "copies": 4, "price": 8},
    5: {"name" : "RDR2", "copies": 15, "price": 10}
}

user_info = {}

def create_account():
    print("\n=============================================================")
    print("              ✩ WELCOME TO THE VIDEO GAME RENTAL ✩         ")
    print("                        ACCOUNT CREATION                    ")
    print("=============================================================\n")
    username = input("Choose a username: ")
    password = input("Create a password: ")
    user_info[username] = {'password': password, 'balance': 0, 'points': 0, 'inventory': []}
    print("Great! Account created successfully. Your wallet balance: $0")

def log_in():
    print("\nLogin")
    username = input("Username: ")
    password = input("Password: ")
    if username in user_info and user_info[username]['password'] == password:
        print("Login successful!")
        return username
    elif username == "admin" and password == "adminpass":
        return "admin"
    else:
        print("Invalid username or password.")
        return None

def rent_game(username):
    print("\nRent games")
    print("Games available for rent:\n")
    for num, game_info in game_library.items():
        print(f'{num}. {game_info["name"]} - copies {game_info["copies"]} - price ${game_info["price"]}')
    rent_choice = input("Enter the number of the game you want to rent (or press Enter to cancel): ")
    if not rent_choice:
        return
    try:
        rent_choice = int(rent_choice)
        if rent_choice in game_library:
            game_info = game_library[rent_choice]
            if game_info["copies"] > 0:
                game_price = game_info["price"]
                if user_info[username]['balance'] >= game_price:
                    game_name = game_info["name"]
                    game_library[rent_choice]["copies"] -= 1
                    user_info[username]['inventory'].append(game_name)
                    user_info[username]['balance'] -= game_price
                    print("Rent successful!")
                    print(f'Your new wallet balance: ${user_info[username]["balance"]}')
                    
                    points_earned = game_price // 2
                    user_info[username]['points'] += points_earned
                    print(f'You earned {points_earned} points!')
                    
                    if user_info[username]['points'] >= 3:
                        free_game_count = user_info[username]['points'] // 3
                        user_info[username]['points'] %= 3
                        print(f'Congratulations! You earned {free_game_count} free game(s)!')
                else:
                    print("Sorry, you have insufficient funds to rent this game.")
            else:
                print("Sorry, there are no more copies available for this game.")
        else:
            print("Invalid game number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def return_game(username):
    print("\nReturn a game")
    print("Games in your inventory:\n")
    for index, game_name in enumerate(user_info[username]['inventory'], 1):
        print(f'{index}. {game_name}')
    return_choice = input("Enter the number of the game you want to return (or press Enter to cancel): ")
    if return_choice.isdigit():
        return_choice = int(return_choice)
        if 1 <= return_choice <= len(user_info[username]['inventory']):
            game_name = user_info[username]['inventory'][return_choice - 1]
            for game_id, game_info in game_library.items():
                if game_info['name'] == game_name:
                    game_info["copies"] += 1
                    user_info[username]['inventory'].remove(game_name)
                    print("Return successful!")
                    return
            print("Game not found in the library.")
        else:
            print("Invalid game number.")
    else:
        print("Invalid input. Please enter a number.")

def top_up_balance(username):
    print("\nTop-up balance")
    amount = input("Enter the amount to top-up: $")
    if amount.isdigit():
        amount = float(amount)
        if amount > 0:
            user_info[username]['balance'] += amount
            print(f'Your new wallet balance: ${user_info[username]["balance"]}')
        else:
            print("Invalid amount. Please enter a valid amount.")
    else:
        print("Invalid input. Please enter a number.")

def display_inventory(username):
    print("\nInventory")
    print("Your rented games:")
    for game in user_info[username]['inventory']:
        print(game)

def update_game_details():
    print("\nUpdate game details")
    print("Games available for update:\n")
    for num, game_info in game_library.items():
        print(f'{num}. {game_info["name"]}')
    game_choice = input("Enter the number of the game you want to update (or press Enter to cancel): ")
    if game_choice.isdigit():
        game_choice = int(game_choice)
        if game_choice in game_library:
            print(f"\nSelected game: {game_library[game_choice]['name']}\n")
            print("1. Update copies")
            print("2. Update price")
            option = input("Enter your choice: ")
            if option == "1":
                new_value = input("Enter the new number of copies: ")
                if new_value.isdigit():
                    new_copies = int(new_value)
                    if new_copies >= 0:
                        game_library[game_choice]["copies"] = new_copies
                        print("Copies updated successfully!")
                    else:
                        print("Invalid number of copies.")
                else:
                    print("Invalid input. Please enter a number.")
            elif option == "2":
                new_value = input("Enter the new price: $")
                if new_value.replace(".", "", 1).isdigit():
                    new_price = float(new_value)
                    if new_price >= 0:
                        game_library[game_choice]["price"] = new_price
                        print("Price updated successfully!")
                    else:
                        print("Invalid price.")
                else:
                    print("Invalid input. Please enter a number.")
            else:
                print("Invalid option.")
        else:
            print("Invalid game number.")
    else:
        print("Invalid input. Please enter a number.")

def admin_menu():
    while True:
        print("\nAdmin menu")
        print("1. Update game details")
        print("2. Log out")

        choice = input("Enter your choice: ")
        if choice == "1":
            update_game_details()
        elif choice == "2":
            return
        else:
            print("Invalid input. Please enter a valid option.")

def user_menu(username):
    while True:
        print("\n=============================================================")
        print("           🕹✩ WELCOME TO THE VIDEO GAME RENTAL ✩🕹      ")
        print("        NEW GAME ARRIVAL: Red Dead Redemption 2 (RDR2)    ")
        print("=============================================================\n")
        print("\nUser menu")
        print("1. Rent a game")
        print("2. Return a game")
        print("3. Top-up balance")
        print("4. Display inventory")
        print("5. Log out")

        choice = input("Enter your choice: ")
        if choice == "1":
            rent_game(username)
        elif choice == "2":
            return_game(username)
        elif choice == "3":
            top_up_balance(username)
        elif choice == "4":
            display_inventory(username)
        elif choice == "5":
            return
        else:
            print("Invalid input. Please enter a valid option.")

def main():
    while True:
        print("\n==========================================================")
        print("              ✩ WELCOME TO THE VIDEO GAME RENTAL ✩         ")
        print("              CREATE AN ACCOUNT TO START OR LOG IN          ")
        print("==========================================================\n")
        print("1. Sign up")
        print("2. Log in")
        print("3. Admin log in")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            username = log_in()
            if username:
                user_menu(username)
        elif choice == "3":
            admin_menu()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please enter a valid option.")

main()
