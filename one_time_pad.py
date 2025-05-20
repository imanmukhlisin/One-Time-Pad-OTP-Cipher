import random
import string

def generate_key(length):
    """Generate a random key of uppercase letters."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
def text_to_numbers(text):
    """Convert A-Z to 0-25"""
    return [ord(c) - ord('A') for c in text]
def numbers_to_text(numbers):
    """Convert 0-25 to A-Z"""
    return ''.join(chr(n + ord('A')) for n in numbers)
def otp_encrypt(plaintext, key):
    plain_nums = text_to_numbers(plaintext)
    key_nums = text_to_numbers(key)
    cipher_nums = [(p + k) % 26 for p, k in zip(plain_nums, key_nums)]
    return numbers_to_text(cipher_nums)
def otp_decrypt(ciphertext, key):
    cipher_nums = text_to_numbers(ciphertext)
    key_nums = text_to_numbers(key)
    plain_nums = [(c - k + 26) % 26 for c, k in zip(cipher_nums, key_nums)]
    return numbers_to_text(plain_nums)
def clean_input(text):
    """Uppercase and remove non-letter characters."""
    return ''.join(filter(str.isalpha, text.upper()))

if __name__ == "__main__":
    print("=== One-Time Pad Cipher ===")
    mode = input("Mode (encrypt/decrypt): ").strip().lower()

    if mode == "encrypt":
        plaintext = clean_input(input("Enter plaintext: "))
        key = generate_key(len(plaintext))
        ciphertext = otp_encrypt(plaintext, key)
        print("\n--- Encryption Result ---")
        print("Plaintext :", plaintext)
        print("Key       :", key)
        print("Ciphertext:", ciphertext)

    elif mode == "decrypt":
        ciphertext = clean_input(input("Enter ciphertext: "))
        key = clean_input(input("Enter key (same length): "))
        if len(ciphertext) != len(key):
            print("Error: Key length must match ciphertext length.")
        else:
            plaintext = otp_decrypt(ciphertext, key)
            print("\n--- Decryption Result ---")
            print("Ciphertext:", ciphertext)
            print("Key       :", key)
            print("Plaintext :", plaintext)
    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")