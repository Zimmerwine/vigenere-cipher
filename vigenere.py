def vigenere(text, key, mode = 1):
    key_expanded = '' 
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            key_expanded += key[key_index % key_length]
            key_index += 1
        else:
            key_expanded += char

    result = ''
    key_index = 0
    for i, char in enumerate(text):
        if char.isalpha():
            new_key = ord(key_expanded[key_index].upper()) - ord('A')
            shift = new_key if mode == 1 else -new_key
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char

    return result

while True:
    print('1. Encrypt')
    print('2. Decrypt')
    choice = int(input('Choose an option : '))
    if choice == 1:
        text = str(input('Input your plain text here : '))
        key = str(input('Input your key here : '))
        encrypted = vigenere(text, key, mode=1)
        print(f'text : {text}, cipher : {encrypted}')
    elif choice == 2:
        cipher = str(input('Input your cipher here : '))
        key = str(input('Input your key here : '))
        decrypted = vigenere(cipher, key, mode=-1)
        print(f'Cipher : {cipher}, text = {decrypted}')
    else:
        print('Your input is invalid, Try Again')    
    

       
