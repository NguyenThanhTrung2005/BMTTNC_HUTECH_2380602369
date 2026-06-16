class PlayFairCipher:

    def __init__(self):
        pass

    def validate_key(self, key):
        if key is None:
            raise ValueError("Khóa không được để trống")

        if not isinstance(key, str):
            raise ValueError("Khóa phải là chuỗi ký tự")

        if key.strip() == "":
            raise ValueError("Khóa không được chỉ chứa khoảng trắng")

        key_no_space = key.replace(" ", "")

        if not key_no_space.isascii() or not key_no_space.isalpha():
            raise ValueError("Khóa chỉ được chứa chữ cái tiếng Anh A-Z")

    def validate_plain_text(self, plain_text):
        if plain_text is None:
            raise ValueError("Plain text không được để trống")

        if not isinstance(plain_text, str):
            raise ValueError("Plain text phải là chuỗi ký tự")

        if plain_text.strip() == "":
            raise ValueError("Plain text không được chỉ chứa khoảng trắng")

        plain_text_no_space = plain_text.replace(" ", "")

        if plain_text_no_space == "":
            raise ValueError("Plain text phải chứa ít nhất một chữ cái")

        if not plain_text_no_space.isascii() or not plain_text_no_space.isalpha():
            raise ValueError("Plain text chỉ được chứa chữ cái tiếng Anh A-Z và khoảng trắng")

    def validate_cipher_text(self, cipher_text):
        if cipher_text is None:
            raise ValueError("Cipher text không được để trống")

        if not isinstance(cipher_text, str):
            raise ValueError("Cipher text phải là chuỗi ký tự")

        if cipher_text.strip() == "":
            raise ValueError("Cipher text không được chỉ chứa khoảng trắng")

        cipher_text_no_space = cipher_text.replace(" ", "")

        if cipher_text_no_space == "":
            raise ValueError("Cipher text phải chứa ít nhất một chữ cái")

        if not cipher_text_no_space.isascii() or not cipher_text_no_space.isalpha():
            raise ValueError("Cipher text chỉ được chứa chữ cái tiếng Anh A-Z và khoảng trắng")

        if len(cipher_text_no_space) % 2 != 0:
            raise ValueError("Độ dài Cipher text sau khi bỏ khoảng trắng phải là số chẵn")

    def validate_matrix(self, matrix):
        if matrix is None:
            raise ValueError("Ma trận Playfair không được để trống")

        if not isinstance(matrix, list):
            raise ValueError("Ma trận Playfair không hợp lệ")

        if len(matrix) != 5:
            raise ValueError("Ma trận Playfair phải có 5 dòng")

        for row in matrix:
            if not isinstance(row, list):
                raise ValueError("Mỗi dòng của ma trận Playfair phải là danh sách")

            if len(row) != 5:
                raise ValueError("Mỗi dòng của ma trận Playfair phải có 5 ký tự")

    def create_playfair_matrix(self, key):
        self.validate_key(key)

        key = key.upper().replace("J", "I").replace(" ", "")

        unique_key = ""

        for char in key:
            if char not in unique_key:
                unique_key += char

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix = list(unique_key)

        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)

        playfair_matrix = [
            matrix[i:i + 5]
            for i in range(0, 25, 5)
        ]

        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        self.validate_matrix(matrix)

        if letter is None:
            raise ValueError("Ký tự cần tìm không được để trống")

        if not isinstance(letter, str):
            raise ValueError("Ký tự cần tìm phải là chuỗi")

        if len(letter) != 1:
            raise ValueError("Chỉ được tìm một ký tự trong ma trận")

        letter = letter.upper().replace("J", "I")

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

        raise ValueError(f"Ký tự '{letter}' không tồn tại trong ma trận Playfair")

    def prepare_plain_text(self, plain_text):
        plain_text = plain_text.replace(" ", "")
        plain_text = plain_text.upper().replace("J", "I")

        prepared_text = ""
        i = 0

        while i < len(plain_text):
            char1 = plain_text[i]

            if i + 1 < len(plain_text):
                char2 = plain_text[i + 1]

                if char1 == char2:
                    prepared_text += char1 + "X"
                    i += 1
                else:
                    prepared_text += char1 + char2
                    i += 2
            else:
                prepared_text += char1 + "X"
                i += 1

        return prepared_text

    def playfair_encrypt(self, plain_text, matrix):
        self.validate_plain_text(plain_text)
        self.validate_matrix(matrix)

        plain_text = self.prepare_plain_text(plain_text)

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]

            row1, col1 = self.find_letter_coords(
                matrix,
                pair[0]
            )

            row2, col2 = self.find_letter_coords(
                matrix,
                pair[1]
            )

            if row1 == row2:
                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5]
                    +
                    matrix[row2][(col2 + 1) % 5]
                )

            elif col1 == col2:
                encrypted_text += (
                    matrix[(row1 + 1) % 5][col1]
                    +
                    matrix[(row2 + 1) % 5][col2]
                )

            else:
                encrypted_text += (
                    matrix[row1][col2]
                    +
                    matrix[row2][col1]
                )

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        self.validate_cipher_text(cipher_text)
        self.validate_matrix(matrix)

        cipher_text = cipher_text.replace(" ", "")
        cipher_text = cipher_text.upper().replace("J", "I")

        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]

            row1, col1 = self.find_letter_coords(
                matrix,
                pair[0]
            )

            row2, col2 = self.find_letter_coords(
                matrix,
                pair[1]
            )

            if row1 == row2:
                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5]
                    +
                    matrix[row2][(col2 - 1) % 5]
                )

            elif col1 == col2:
                decrypted_text += (
                    matrix[(row1 - 1) % 5][col1]
                    +
                    matrix[(row2 - 1) % 5][col2]
                )

            else:
                decrypted_text += (
                    matrix[row1][col2]
                    +
                    matrix[row2][col1]
                )

        banro = ""

        for i in range(0, len(decrypted_text)):
            current_char = decrypted_text[i]

            if (
                current_char == "X"
                and i > 0
                and i < len(decrypted_text) - 1
                and decrypted_text[i - 1] == decrypted_text[i + 1]
            ):
                continue

            banro += current_char

        if banro.endswith("X"):
            banro = banro[:-1]

        return banro