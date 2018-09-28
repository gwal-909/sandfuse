def ceasar_cipher(in_text, shift):
    result_text = ''

    for letter in range(len(in_text)): # TODO: use enum instead
        char = in_text[letter]

        if char.isupper():
            result_text += chr((ord(char) + shift - 65) % 36 + 65)
            # result_text += chr((ord(char) + shift) % 36)
        else:
            result_text += chr((ord(char) + shift - 97) % 26 + 97)
            # result_text += chr((ord(char) + shift) % 26)
    return result_text

def main():
    text = 'WeAreDOOMED'  # TODO: allow for spaces in input.
    
    shift = 4
    ciphered_message = ceasar_cipher(text, shift)
    print('Input: ', text)
    print('Shift count: ', shift)
    print('Ciphered text: ', ciphered_message)  

if __name__ == '__main__':
    main()
