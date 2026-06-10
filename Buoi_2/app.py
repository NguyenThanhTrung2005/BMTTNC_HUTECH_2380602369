from flask import Flask, render_template, request
from html import escape

from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)


# ================= HÀM HỖ TRỢ =================

def lay_gia_tri_form(field_name, ten_truong):
    value = request.form.get(field_name, "")

    if value is None or value.strip() == "":
        raise ValueError(f"{ten_truong} không được để trống")

    return value


def lay_khoa_so_nguyen(field_name):
    key = lay_gia_tri_form(field_name, "Khóa")

    try:
        return int(key)
    except ValueError:
        raise ValueError("Khóa phải là số nguyên")


def hien_thi_ket_qua(tieu_de, text, key, result, back_url):
    return f"""
    <h3>{escape(tieu_de)}</h3>
    <p><b>Text:</b> {escape(str(text))}</p>
    <p><b>Key:</b> {escape(str(key))}</p>
    <p><b>Result:</b> {escape(str(result))}</p>
    <br>
    <a href="{back_url}">Quay lại</a>
    """


def hien_thi_loi(tieu_de, error, back_url):
    return f"""
    <h3 style="color:red;">{escape(tieu_de)}</h3>
    <p><b>Lỗi:</b> {escape(str(error))}</p>
    <br>
    <a href="{back_url}">Quay lại</a>
    """


# ================= HOME =================

@app.route('/')
def home():
    return render_template('index.html')


# ================= CAESAR =================

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')


@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        text = lay_gia_tri_form('inputPlainText', 'Plain text')
        key = lay_khoa_so_nguyen('inputKeyPlain')

        cipher = CaesarCipher()
        result = cipher.encrypt_text(text, key)

        return hien_thi_ket_qua(
            "Caesar Encrypt Result",
            text,
            key,
            result,
            "/caesar"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi mã hóa Caesar",
            e,
            "/caesar"
        )


@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        text = lay_gia_tri_form('inputCipherText', 'Cipher text')
        key = lay_khoa_so_nguyen('inputKeyCipher')

        cipher = CaesarCipher()
        result = cipher.decrypt_text(text, key)

        return hien_thi_ket_qua(
            "Caesar Decrypt Result",
            text,
            key,
            result,
            "/caesar"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi giải mã Caesar",
            e,
            "/caesar"
        )


# ================= PLAYFAIR =================

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    try:
        key = lay_gia_tri_form('inputKeyMatrix', 'Khóa')

        cipher = PlayFairCipher()
        matrix = cipher.create_playfair_matrix(key)

        matrix_html = "<table class='table table-bordered text-center' style='width: 300px;'>"

        for row in matrix:
            matrix_html += "<tr>"
            for char in row:
                matrix_html += f"<td><b>{escape(str(char))}</b></td>"
            matrix_html += "</tr>"

        matrix_html += "</table>"

        return f"""
        <h3>Playfair Matrix Result</h3>
        <p><b>Key:</b> {escape(str(key))}</p>
        {matrix_html}

        <br>

        <a href="/playfair">
            <button>Quay lại Playfair</button>
        </a>

        <a href="/">
            <button>Trang chủ</button>
        </a>
        """

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi tạo ma trận Playfair",
            e,
            "/playfair"
        )

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        text = lay_gia_tri_form('inputPlainText', 'Plain text')
        key = lay_gia_tri_form('inputKey', 'Khóa')

        cipher = PlayFairCipher()
        matrix = cipher.create_playfair_matrix(key)
        result = cipher.playfair_encrypt(text, matrix)

        return hien_thi_ket_qua(
            "Playfair Encrypt Result",
            text,
            key,
            result,
            "/playfair"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi mã hóa Playfair",
            e,
            "/playfair"
        )


@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        text = lay_gia_tri_form('inputCipherText', 'Cipher text')
        key = lay_gia_tri_form('inputKey', 'Khóa')

        cipher = PlayFairCipher()
        matrix = cipher.create_playfair_matrix(key)
        result = cipher.playfair_decrypt(text, matrix)

        return hien_thi_ket_qua(
            "Playfair Decrypt Result",
            text,
            key,
            result,
            "/playfair"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi giải mã Playfair",
            e,
            "/playfair"
        )


# ================= RAIL FENCE =================

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')


@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        text = lay_gia_tri_form('inputPlainText', 'Plain text')
        key = lay_khoa_so_nguyen('inputKey')

        cipher = RailFenceCipher()
        result = cipher.rail_fence_encrypt(text, key)

        return hien_thi_ket_qua(
            "Rail Fence Encrypt Result",
            text,
            key,
            result,
            "/railfence"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi mã hóa Rail Fence",
            e,
            "/railfence"
        )


@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        text = lay_gia_tri_form('inputCipherText', 'Cipher text')
        key = lay_khoa_so_nguyen('inputKey')

        cipher = RailFenceCipher()
        result = cipher.rail_fence_decrypt(text, key)

        return hien_thi_ket_qua(
            "Rail Fence Decrypt Result",
            text,
            key,
            result,
            "/railfence"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi giải mã Rail Fence",
            e,
            "/railfence"
        )


# ================= VIGENERE =================

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')


@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        text = lay_gia_tri_form('inputPlainText', 'Plain text')
        key = lay_gia_tri_form('inputKey', 'Khóa')

        cipher = VigenereCipher()
        result = cipher.vigenere_encrypt(text, key)

        return hien_thi_ket_qua(
            "Vigenere Encrypt Result",
            text,
            key,
            result,
            "/vigenere"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi mã hóa Vigenere",
            e,
            "/vigenere"
        )


@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        text = lay_gia_tri_form('inputCipherText', 'Cipher text')
        key = lay_gia_tri_form('inputKey', 'Khóa')

        cipher = VigenereCipher()
        result = cipher.vigenere_decrypt(text, key)

        return hien_thi_ket_qua(
            "Vigenere Decrypt Result",
            text,
            key,
            result,
            "/vigenere"
        )

    except ValueError as e:
        return hien_thi_loi(
            "Lỗi giải mã Vigenere",
            e,
            "/vigenere"
        )


# ================= MAIN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)