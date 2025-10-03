# Create a logo and print to console
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

# Create a list with all the letters from the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a variable for restarting the program
restarting = "yes"

# Create the encrypt/decrypt function
def caesar(original_text, shift_amount, encode_or_decode):

    # Create an empty variable (string) for the output text
    output_text = ""

    # Loop over every char in original text
    for letter in original_text:
        
        # Check if the user want to encode/decode
        if encode_or_decode == "decode":
            
            # Set shift amount to minus
            shift_amount *= -1

        # Get index number of every character and change the position in alphabet
        shifted_position = alphabet.index(letter) + shift_amount

        # Check if new position is above 26
        shifted_position %= len(alphabet)

        # assign new character to the empty string
        output_text += alphabet[shifted_position]

    # Output new word to console
    print(f"Here is the {encode_or_decode}d result: {output_text}\n")
 

# Check if restart variable is set to yes
while restarting == "yes":

    # Ask inp print(restarting)ut questions
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


    # Ask the user to restart program
    restart = input("Hit Yes to end the program or No to start again.\n").lower()

    # Set restart variable to no to end the program
    if restart == "no":
        restarting = "no"
