# Kevin Montero
# Lab 09: Software Engineering

def encode(password): # Encode Password Function
    encoded_pass = "" # Initializes empty string to store encoded digits
    for digit in password: # Iterates through each digit in the password and shifts each number up by 3
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_pass += encoded_digit
    return encoded_pass # Returns Encoded Password

def decode(password):
    decodedpassword=""
    for digit in password: #iterates through each digit, subtracting each by 3
        decoded_digit = str((int(digit) - 3) % 10) #applies floor of 10
        decodedpassword += decoded_digit
    return decodedpassword  # Returns Encoded Password

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
            decodedpassword=decode(password)
            print(f"The encoded password is {password}, and the original password is {decodedpassword}")
        elif option == 3:
            exit()