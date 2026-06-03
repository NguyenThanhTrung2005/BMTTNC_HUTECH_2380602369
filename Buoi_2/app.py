from flask import Flask, render_template, request

from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/caesar')
def caesar():
    return render_template('caesar.html')


@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():

    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    cipher = CaesarCipher()

    result = cipher.encrypt_text(text, key)

    return f"""
    <h3>Caesar Encrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():

    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    cipher = CaesarCipher()

    result = cipher.decrypt_text(text, key)

    return f"""
    <h3>Caesar Decrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')


@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():

    text = request.form['inputPlainText']
    key = request.form['inputKey']

    cipher = PlayFairCipher()

    matrix = cipher.create_playfair_matrix(key)

    result = cipher.playfair_encrypt(text, matrix)

    return f"""
    <h3>Playfair Encrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():

    text = request.form['inputCipherText']
    key = request.form['inputKey']

    cipher = PlayFairCipher()

    matrix = cipher.create_playfair_matrix(key)

    result = cipher.playfair_decrypt(text, matrix)

    return f"""
    <h3>Playfair Decrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


# ================= RAIL FENCE =================

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')


@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():

    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])

    cipher = RailFenceCipher()

    result = cipher.rail_fence_encrypt(text, key)

    return f"""
    <h3>Rail Fence Encrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():

    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])

    cipher = RailFenceCipher()

    result = cipher.rail_fence_decrypt(text, key)

    return f"""
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


# ================= VIGENERE =================

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')


@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():

    text = request.form['inputPlainText']
    key = request.form['inputKey']

    cipher = VigenereCipher()

    result = cipher.vigenere_encrypt(text, key)

    return f"""
    <h3>Vigenere Encrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():

    text = request.form['inputCipherText']
    key = request.form['inputKey']

    cipher = VigenereCipher()

    result = cipher.vigenere_decrypt(text, key)

    return f"""
    <h3>Vigenere Decrypt Result</h3>
    Text: {text}<br>
    Key: {key}<br>
    Result: {result}
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)