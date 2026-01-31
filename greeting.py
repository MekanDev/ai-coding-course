RESET = "\033[0m"

while True:
    name = input("\033[35mType your name: \033[34m").capitalize()

    if any(ch.isdigit() for ch in name) or any(not ch.isalnum() for ch in name):
        print(f"\033[31mDon't type numbers and symbols! {RESET}\n")
    elif not name:
        print(f"\033[31mWrite your name! {RESET}\n")
    else:
        print(f"\033[33mWelcome, \033[34m{name}! {RESET}")
        break