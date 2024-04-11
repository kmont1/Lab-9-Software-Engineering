# Kevin Montero
# Lab 09: Software Engineering

def encode(password): # Encode Password Function
    encoded_pass = "" # Initializes empty string to store encoded digits
    for digit in password: # Iterates through each digit in the password and shifts each number up by 3
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_pass += encoded_digit
    return encoded_pass # Returns Encoded Password

if __name__ == "__main__":
    while True:
        print("Menu\n-------------"
              "\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Enter password to encode: ")
            password = encode(password)
            print(f"Your encoded password is {password}")
        elif option == 2:
            pass
        elif option == 3:
            exit()