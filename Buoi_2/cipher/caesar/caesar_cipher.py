from cipher.caesar import ALPHABET


class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def validate_text(self, text: str, text_type: str):
        if text is None:
            raise ValueError(f"{text_type} không được để trống")

        if not isinstance(text, str):
            raise ValueError(f"{text_type} phải là chuỗi ký tự")

        if text.strip() == "":
            raise ValueError(f"{text_type} không được chỉ chứa khoảng trắng")

        if not any(char.upper() in self.alphabet for char in text):
            raise ValueError(f"{text_type} phải chứa ít nhất một chữ cái")

    def validate_key(self, key: int):
        if key is None:
            raise ValueError("Khóa không được để trống")

        if not isinstance(key, int):
            raise ValueError("Khóa phải là số nguyên")

        if key < 1 or key > 25:
            raise ValueError("Khóa phải nằm trong khoảng từ 1 đến 25")

    def encrypt_text(self, text: str, key: int) -> str:
        self.validate_text(text, "Plain text")
        self.validate_key(key)

        alphabet_len = len(self.alphabet)

        key = key % alphabet_len
        text = text.upper()

        encrypted_text = []

        for letter in text:
            if letter not in self.alphabet:
                encrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]

            encrypted_text.append(output_letter)

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        self.validate_text(text, "Cipher text")
        self.validate_key(key)

        alphabet_len = len(self.alphabet)

        key = key % alphabet_len
        text = text.upper()

        decrypted_text = []

        for letter in text:
            if letter not in self.alphabet:
                decrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]

            decrypted_text.append(output_letter)

        return "".join(decrypted_text)