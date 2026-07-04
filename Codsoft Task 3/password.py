import string
import secrets
import sys

# ANSI escape codes for clean terminal styling
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"

def print_banner():
    banner = f"""
{BLUE}{BOLD}====================================================
           SECURE PASSWORD GENERATOR
===================================================={RESET}
"""
    print(banner)

def get_boolean_input(prompt, default=True):
    default_str = " [Y/n]: " if default else " [y/N]: "
    while True:
        try:
            val = input(f"{CYAN}{prompt}{default_str}{RESET}").strip().lower()
            if not val:
                return default
            if val in ('y', 'yes'):
                return True
            if val in ('n', 'no'):
                return False
            print(f"{YELLOW}Please enter 'y' or 'n'.{RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{RED}Operation cancelled.{RESET}")
            sys.exit(0)

def get_password_length():
    while True:
        try:
            val_str = input(f"{CYAN}Enter the desired password length (minimum 4, recommended 12+): {RESET}").strip()
            if not val_str:
                print(f"{YELLOW}Length cannot be empty. Please enter a number.{RESET}")
                continue
            val = int(val_str)
            if val < 4:
                print(f"{YELLOW}Password length must be at least 4 for security and structure.{RESET}")
                continue
            return val
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid whole number.{RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{RED}Operation cancelled.{RESET}")
            sys.exit(0)

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Prepare the pools of characters
    pools = []
    guaranteed = []

    if use_upper:
        pools.append(string.ascii_uppercase)
        # Ensure at least one uppercase letter is in the password
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        pools.append(string.ascii_lowercase)
        # Ensure at least one lowercase letter is in the password
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        pools.append(string.digits)
        # Ensure at least one digit is in the password
        guaranteed.append(secrets.choice(string.digits))
    if use_special:
        special_chars = "!@#$%^&*()_+=-[]{}|;:',.<>?/"
        pools.append(special_chars)
        # Ensure at least one special character is in the password
        guaranteed.append(secrets.choice(special_chars))

    if not pools:
        return None

    # Combine all selected pools for the remaining characters
    all_chars = "".join(pools)
    
    # Calculate how many more random characters we need
    remaining_length = length - len(guaranteed)
    
    # Generate the remaining characters
    random_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]
    
    # Combine guaranteed characters and the remaining random characters
    password_list = guaranteed + random_chars
    
    # Shuffle the list securely to ensure the guaranteed characters are not at predictable positions
    secrets.SystemRandom().shuffle(password_list)
    
    return "".join(password_list)

def main():
    # Enable ANSI escape sequences on Windows if needed (handled automatically by modern terminal/win10+)
    # Import ctypes to enable virtual terminal processing if on Windows
    if sys.platform == 'win32':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

    print_banner()

    while True:
        length = get_password_length()
        
        print(f"\n{BOLD}Select character sets to include:{RESET}")
        use_upper = get_boolean_input("Include uppercase letters (A-Z)?", default=True)
        use_lower = get_boolean_input("Include lowercase letters (a-z)?", default=True)
        use_digits = get_boolean_input("Include numbers (0-9)?", default=True)
        use_special = get_boolean_input("Include special characters (!@#...)?", default=True)

        if not (use_upper or use_lower or use_digits or use_special):
            print(f"\n{RED}Error: You must select at least one character set.{RESET}")
            print(f"{YELLOW}Let's try again.\n{RESET}")
            continue

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        
        print(f"\n{GREEN}{BOLD}Generated Password: {RESET}{BOLD}{password}{RESET}\n")

        if not get_boolean_input("Would you like to generate another password?", default=False):
            print(f"\n{BLUE}Thank you for using the Secure Password Generator. Goodbye!{RESET}")
            break
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()