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
            if mode == 1:
                shift = new_key
            else: 
                shift = -new_key
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
        key_index += 1

    return result

text = str(input('Input your plain text here : '))
key = str(input('Input your key here : '))
encrypted = vigenere(text, key)
print(f'text : {text}, cipher : {encrypted}')
decrypted = vigenere(encrypted, key, -1)
print(f'cipher : {encrypted}, text = {decrypted}')
    

       
