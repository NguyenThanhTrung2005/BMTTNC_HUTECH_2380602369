class VigenereCipher:
    def __init__(self):
        pass

    def validate_key(self, key):
        if key is None:
            raise ValueError("Khóa không được để trống")

        if not isinstance(key, str):
            raise ValueError("Khóa phải là chuỗi ký tự")

        if key.strip() == "":
            raise ValueError("Khóa không được chỉ chứa khoảng trắng")

        if not key.isalpha():
            raise ValueError("Khóa chỉ được chứa chữ cái")

    def validate_text(self, text, text_type):
        if text is None:
            raise ValueError(f"{text_type} không được để trống")

        if not isinstance(text, str):
            raise ValueError(f"{text_type} phải là chuỗi ký tự")

        if text.strip() == "":
            raise ValueError(f"{text_type} không được chỉ chứa khoảng trắng")

        if not any(char.isalpha() for char in text):
            raise ValueError(f"{text_type} phải chứa ít nhất một chữ cái")

    def vigenere_encrypt(self, plain_text, key):
        self.validate_text(plain_text, "Plain text")
        self.validate_key(key)

        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    encrypted_text += chr(
                        (ord(char) - ord('A') + key_shift) % 26 + ord('A')
                    )
                else:
                    encrypted_text += chr(
                        (ord(char) - ord('a') + key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                encrypted_text += char

        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        self.validate_text(encrypted_text, "Cipher text")
        self.validate_key(key)

        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    decrypted_text += chr(
                        (ord(char) - ord('A') - key_shift) % 26 + ord('A')
                    )
                else:
                    decrypted_text += chr(
                        (ord(char) - ord('a') - key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text