logo = logo = """           
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

alphabet = alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text, shift):
    ceaser_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            ceaser_text += alphabet[alphabet.index(letter) + shift]
        else:
            ceaser_text += letter
    print(f"Here's the {direction} result:", ceaser_text)


# def encrypt(direction, text, shift):
#     encoded_msg = []
#     for letter in text:
#         chiper_letter = alphabet[alphabet.index(letter) + shift]
#         encoded_msg.append(chiper_letter)
#     print(f"Here's the {direction} result:", ''.join(encoded_msg))

# def decrypt(direction, text, shift):
#     decoded_msg = []
#     for letter in text:
#         decode_letter = alphabet[alphabet.index(letter) - shift]
#         decoded_msg.append(decode_letter)
#     print(f"Here's the {direction} result:", ''.join(decoded_msg))

user_flag = False
print(logo)
while not user_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if direction == "encode":
    #     encrypt(direction, text, shift)
    # else:
    #     decrypt(direction, text, shift)
    shift %= 26
    ceaser(direction, text, shift)
    user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if user_choice == "no" or user_choice != "yes":
        user_flag = True