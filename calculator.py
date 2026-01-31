RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def main():
    while True:
        digit1 = (input("\nType first digit: "))
        digit2 = (input("Type second digit: "))
        try:
            a = float(digit1)
            b = float(digit2)
            break
        except ValueError:
            print(f"{RED}Type only integer and float!{RESET}")

    print(f"\n{GREEN}Type 1 for '-'")
    print("Type 2 for '+'")
    print("Type 3 for '/'")
    print("Type 4 for '*'")
    print(f"Type 5 for '^'{RESET}\n")

    while True:
        try:
            op = int(input("Choose operator: "))

            if op >= 1 and op <= 5:
                if op == 1:
                    print(f"{YELLOW}Result: {a-b}{RESET}\n")
                elif op == 2:
                    print(f"{YELLOW}Result: {a+b}{RESET}\n")
                elif op == 3:
                    if b == 0:
                        print(f"{RED}Can't divide to zero!{RESET}\n")
                    else:
                        print(f"{YELLOW}Result: {a/b}{RESET}\n")
                elif op == 4:
                    print(f"{YELLOW}Result: {a*b}{RESET}\n")
                else:
                    print(f"{YELLOW}Result: {a**b}{RESET}\n")
                break
            else:
                print(f"{RED}Undefined operation!{RESET}\n")
        except ValueError:
            print(f"{RED}Only integer!{RESET}\n")

main()