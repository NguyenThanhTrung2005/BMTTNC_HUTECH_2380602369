class PlayFairCipher:

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):

        # Kiểm tra key
        if not key:
            raise ValueError("Key cannot be empty")

        if not key.isalpha():
            raise ValueError("Key must contain letters only")

        key = key.upper().replace("J", "I")

        # Loại bỏ ký tự trùng lặp trong key
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

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

        raise ValueError(f"Letter '{letter}' not found in matrix")

    def playfair_encrypt(self, plain_text, matrix):

        # Kiểm tra dữ liệu đầu vào
        if not plain_text:
            raise ValueError("Plain text cannot be empty")

        plain_text = plain_text.replace(" ", "")

        if not plain_text.isalpha():
            raise ValueError(
                "Plain text must contain letters only"
            )

        plain_text = plain_text.upper().replace("J", "I")

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):

            pair = plain_text[i:i + 2]

            if len(pair) == 1:
                pair += "X"

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

        # Kiểm tra dữ liệu đầu vào
        if not cipher_text:
            raise ValueError("Cipher text cannot be empty")

        cipher_text = cipher_text.replace(" ", "")

        if not cipher_text.isalpha():
            raise ValueError(
                "Cipher text must contain letters only"
            )

        if len(cipher_text) % 2 != 0:
            raise ValueError(
                "Cipher text length must be even"
            )

        cipher_text = cipher_text.upper()

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

        # Khôi phục bản rõ giống code gốc
        banro = ""

        for i in range(0, len(decrypted_text) - 2, 2):

            if decrypted_text[i] == decrypted_text[i + 2]:
                banro += decrypted_text[i]

            else:
                banro += (
                    decrypted_text[i]
                    +
                    decrypted_text[i + 1]
                )

        if len(decrypted_text) >= 2:

            if decrypted_text[-1] == "X":
                banro += decrypted_text[-2]

            else:
                banro += decrypted_text[-2]
                banro += decrypted_text[-1]

        return banro