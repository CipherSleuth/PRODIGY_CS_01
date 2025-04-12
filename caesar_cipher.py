def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift key (e.g., 3): "))

    if mode == "encrypt":
        print("Encrypted Text:", encrypt(text, shift))
    elif mode == "decrypt":
        print("Decrypted Text:", decrypt(text, shift))
    else:
        print("Invalid mode selected.")
