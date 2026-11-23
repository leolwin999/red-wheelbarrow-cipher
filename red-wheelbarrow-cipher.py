import codecs
import random

# Iconic Mr. Robot quotes displayed randomly upon exiting
MR_ROBOT_QUOTES = [
    "Control is an illusion.",
    "Bonsoir, Elliot.",
    "A bug is never just a mistake. It represents something bigger.",
    "People always make the best exploits.",
    "We are finally awake.",
    "The world itself's just one big hoax.",
    "Give a man a gun and he can rob a bank, but give a man a bank and he can rob the world.",
    "Power belongs to the people that take it."
]

def red_wheelbarrow_encrypt(plaintext: str) -> str:
    """
    Encrypts a message using the Red Wheelbarrow two-step cipher while preserving case:
    1. Apply ROT13 to alphabetic characters.
    2. Convert resulting letters to their A1Z26 numerical positions with case tags:
       - Uppercase letters -> 'U' prefix + 1..26 (e.g., U15)
       - Lowercase letters -> 'L' prefix + 1..26 (e.g., L15)
    
    Tokens within a word are separated by hyphens (-), and spaces are preserved
    to maintain word boundaries.
    """
    try:
        # Step 1: Apply ROT13 transformation to the entire string
        rot13_text = codecs.encode(plaintext, 'rot_13')
        
        encrypted_words = []
        # Split by spaces to preserve word separation
        for word in rot13_text.split(' '):
            converted_chars = []
            for char in word:
                if char.isupper():
                    # Step 2a: Uppercase -> U1 ... U26
                    num = ord(char) - ord('A') + 1
                    converted_chars.append(f"U{num}")
                elif char.islower():
                    # Step 2b: Lowercase -> L1 ... L26
                    num = ord(char) - ord('a') + 1
                    converted_chars.append(f"L{num}")
                elif char.isdigit():
                    # Wrap literal digits in brackets so decryptor doesn't confuse them with A1Z26 codes
                    converted_chars.append(f"[{char}]")
                else:
                    # Keep punctuation or symbols intact
                    converted_chars.append(char)
            
            # Join characters in a word with hyphens unambiguously
            encrypted_words.append('-'.join(converted_chars))
            
        return ' '.join(encrypted_words)
    
    except Exception as e:
        return f"[Encryption Error]: {str(e)}"


def red_wheelbarrow_decrypt(ciphertext: str) -> str:
    """
    Decrypts a message encoded with the Red Wheelbarrow two-step cipher:
    1. Convert A1Z26 tokens back into letters (U1..U26 -> A..Z, L1..L26 -> a..z, or legacy 1..26 -> A..Z).
    2. Apply ROT13 to reveal the original plaintext with original casing.
    """
    try:
        decrypted_words = []
        
        for word in ciphertext.split(' '):
            # Split cleanly on hyphens since no token uses '-' as a sign anymore
            tokens = word.split('-')
            decoded_chars = []
            
            for token in tokens:
                if not token:
                    continue
                # Check if the token is a wrapped literal digit (e.g., "[6]")
                if token.startswith('[') and token.endswith(']') and token[1:-1].isdigit():
                    decoded_chars.append(token[1:-1])
                # Check if the token is an uppercase alphabet token (U1 to U26)
                elif token.startswith('U') and token[1:].isdigit() and 1 <= int(token[1:]) <= 26:
                    letter = chr(int(token[1:]) + ord('A') - 1)
                    decoded_chars.append(letter)
                # Check if the token is a lowercase alphabet token (L1 to L26)
                elif token.startswith('L') and token[1:].isdigit() and 1 <= int(token[1:]) <= 26:
                    letter = chr(int(token[1:]) + ord('a') - 1)
                    decoded_chars.append(letter)
                # Backward compatibility for plain numbers (1 to 26 -> uppercase)
                elif token.isdigit() and 1 <= int(token) <= 26:
                    letter = chr(int(token) + ord('A') - 1)
                    decoded_chars.append(letter)
                else:
                    # Preserve punctuation, symbols, or unmapped characters
                    decoded_chars.append(token)
                    
            decrypted_words.append(''.join(decoded_chars))
            
        intermediate_text = ' '.join(decrypted_words)
        
        # Step 2: Apply ROT13 again (since ROT13 is its own inverse and preserves case)
        plaintext = codecs.encode(intermediate_text, 'rot_13')
        return plaintext
        
    except Exception as e:
        return f"[Decryption Error]: {str(e)}"


def main():
    """
    Interactive CLI demonstrating the Mr. Robot scene and allowing custom input.
    """
    print("=" * 55)
    print("   RED WHEELBARROW CIPHER UTILITY (ROT13+A1Z26)")
    print("=" * 55)
    
    # Iconic quote demonstrating preserved uppercase, lowercase, and numbers
    sample_message = "Bonsoir Elliot 6"
    print(f"\n[DEMO] Original Message : {sample_message}")
    
    encrypted = red_wheelbarrow_encrypt(sample_message)
    print(f"[DEMO] Encrypted Output : {encrypted}")
    
    decrypted = red_wheelbarrow_decrypt(encrypted)
    print(f"[DEMO] Decrypted Output : {decrypted}")
    print("-" * 55)

    # Interactive mode
    while True:
        print("\nSelect an operation:")
        print("  [1] Encrypt (Plaintext -> ROT13 -> Numbers)")
        print("  [2] Decrypt (Numbers -> Letters -> ROT13)")
        print("  [3] Exit")
        
        choice = input("\nfsociety@mrrobot:~$ ").strip()
        
        if choice == '1':
            msg = input("Enter message to encrypt: ")
            print(f"\n>> Ciphertext: {red_wheelbarrow_encrypt(msg)}")
        elif choice == '2':
            cipher = input("Enter numbers to decrypt (e.g., U15-L2-L1-L6-L2-L22-L5): ")
            print(f"\n>> Plaintext : {red_wheelbarrow_decrypt(cipher)}")
        elif choice == '3':
            quote = random.choice(MR_ROBOT_QUOTES)
            print(f"\nExiting... {quote}")
            break
        else:
            print("\n[!] Invalid selection. Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
