def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decode(text, shift):
    return encode(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Encoder/Decoder!")
    text = input("Enter the text to encode/decode: ")
    shift = int(input("Enter the shift value: "))

    encoded_text = encode(text, shift)
    decoded_text = decode(encoded_text, shift)

    print("\nEncoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)

if __name__ == "__main__":
    main()
