
def caesar_cipher(text, shift, encrypt = True):
    if not isinstance(shift, int):
        return "shift must be an integer"
    elif shift < 1 or shift > 25:
        return "shift must be between 1 and 25"
    elif not encrypt:
        shift  = - shift

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),shifted_alphabet + shifted_alphabet.upper())

    return text.translate(translation_table)

def main():
    print("Enter 0 for Encrypt and 1 for Decrypt: ")
    process  = int(input())
    print("Enter Message: ")
    message = input()
    print("Enter Shift: ")
    shift = int(input())

    if process == 0:
        print("Encrypted Message: \n" , caesar_cipher(message, shift))
    else:
        print("Decrypted Message: \n", caesar_cipher(message, shift, False))

if __name__ == "__main__":
    main()