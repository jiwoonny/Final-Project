import re
def encode_all_1(text):
    """
    Encode all Latin letters to leet speak
    IN: text, str, input text
    OUT: str, leet speak text
    """
    leet_mapping = {
        'A': '4', 'B': '8', 'C': '(', 'D': ')', 'E': '3', 'F': 'ƒ',
        'G': '6', 'H': '#', 'I': '!', 'J': ']', 'K': '|', 'L': '1',
        'M': 'м', 'N': 'и', 'O': 'Ø', 'P': '9', 'Q': '2', 'R': 'Я',
        'S': '5', 'T': '7', 'U': 'µ', 'V': '√', 'W': 'ω', 'X': 'Ж',
        'Y': '¥', 'Z': '%'
    }

    encoded_text = ''
    for char in text:
        if char in leet_mapping:  # Check if the character is in the mapping
            encoded_char = leet_mapping[char.upper()]
            encoded_text += encoded_char
        else:
            encoded_text += ' '
    
    return encoded_text

def decode_all_1(text):
    """
    Decode all leet speak to Latin letters
    IN: text, str, leet speak text
    OUT: str, Latin letters text
    """
    leet_mapping = {
        'A': '4', 'B': '8', 'C': '(', 'D': ')', 'E': '3', 'F': 'ƒ',
        'G': '6', 'H': '#', 'I': '!', 'J': ']', 'K': '|', 'L': '1',
        'M': 'м', 'N': 'и', 'O': 'Ø', 'P': '9', 'Q': '2', 'R': 'Я',
        'S': '5', 'T': '7', 'U': 'µ', 'V': '√', 'W': 'ω', 'X': 'Ж',
        'Y': '¥', 'Z': '%'
    }
    
    # Reverse the dictionary for decoding
    reverse_mapping = {value: key for key, value in leet_mapping.items()}
    
    decoded_text = ''
    
    for char in text:
        if char in reverse_mapping:  # Check if the character is in the reverse mapping
            decoded_char = reverse_mapping[char]
            decoded_text += decoded_char
        else:
            decoded_text += ' ' #for spaces
    return decoded_text

def main():
    english_text = "HELLO HOW ARE YOU DOING"
    print(f"Original English: {english_text}")

    leet_text = encode_all_1(english_text)
    print(f"Coverted text: {leet_text}")

    print(f"Decoded Text: {decode_all_1(leet_text)}")

if __name__ == "__main__":
    main()

