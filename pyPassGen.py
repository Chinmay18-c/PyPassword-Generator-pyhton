import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    password_chars = []

    for _ in range(nr_letters):
        password_chars.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_chars.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_chars.append(random.choice(numbers))

    random.shuffle(password_chars)

    return ''.join(password_chars)


# Example usage:
print(Fore.CYAN + Style.BRIGHT + "Welcome to the PyPassword Generator!")
letters_count = int(input(Fore.YELLOW + "How many letters would you like in your password? "))
symbols_count = int(input(Fore.YELLOW + "How many symbols would you like? "))
numbers_count = int(input(Fore.YELLOW + "How many numbers would you like? "))

final_password = generate_password(letters_count, symbols_count, numbers_count)
print(Fore.GREEN + Style.BRIGHT + f"\nYour password is: {final_password}")
