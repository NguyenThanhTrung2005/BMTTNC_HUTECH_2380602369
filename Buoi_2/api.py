from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)



def get_request_data():
    if request.is_json:
        return request.get_json()
    return request.form


def get_required_value(data, field_name, vietnamese_name):
    value = data.get(field_name, "")

    if value is None or str(value).strip() == "":
        raise ValueError(f"{vietnamese_name} không được để trống")

    return value


def get_integer_key(data, field_name="key"):
    key = get_required_value(data, field_name, "Khóa")

    try:
        return int(key)
    except ValueError:
        raise ValueError("Khóa phải là số nguyên")


@app.route("/")
def home():
    return """
    <h1>API Flask đang chạy</h1>
    <p>Server đã chạy thành công.</p>
    <p>Dùng PyQt5, Postman hoặc Thunder Client để test API.</p>
    """


caesar_cipher = CaesarCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = get_request_data()

        plain_text = get_required_value(data, "plain_text", "Plain text")
        key = get_integer_key(data)

        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)

        return jsonify({
            "encrypted_message": encrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = get_request_data()

        cipher_text = get_required_value(data, "cipher_text", "Cipher text")
        key = get_integer_key(data)

        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)

        return jsonify({
            "decrypted_message": decrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


vigenere_cipher = VigenereCipher()


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        data = get_request_data()

        plain_text = get_required_value(data, "plain_text", "Plain text")
        key = get_required_value(data, "key", "Khóa")

        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)

        return jsonify({
            "encrypted_text": encrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = get_request_data()

        cipher_text = get_required_value(data, "cipher_text", "Cipher text")
        key = get_required_value(data, "key", "Khóa")

        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)

        return jsonify({
            "decrypted_text": decrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


railfence_cipher = RailFenceCipher()


@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        data = get_request_data()

        plain_text = get_required_value(data, "plain_text", "Plain text")
        key = get_integer_key(data)

        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)

        return jsonify({
            "encrypted_text": encrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = get_request_data()

        cipher_text = get_required_value(data, "cipher_text", "Cipher text")
        key = get_integer_key(data)

        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)

        return jsonify({
            "decrypted_text": decrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


playfair_cipher = PlayFairCipher()


@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    try:
        data = get_request_data()

        key = get_required_value(data, "key", "Khóa")

        playfair_matrix = playfair_cipher.create_playfair_matrix(key)

        return jsonify({
            "playfair_matrix": playfair_matrix
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        data = get_request_data()

        plain_text = get_required_value(data, "plain_text", "Plain text")
        key = get_required_value(data, "key", "Khóa")

        playfair_matrix = playfair_cipher.create_playfair_matrix(key)

        encrypted_text = playfair_cipher.playfair_encrypt(
            plain_text,
            playfair_matrix
        )

        return jsonify({
            "encrypted_text": encrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        data = get_request_data()

        cipher_text = get_required_value(data, "cipher_text", "Cipher text")
        key = get_required_value(data, "key", "Khóa")

        playfair_matrix = playfair_cipher.create_playfair_matrix(key)

        decrypted_text = playfair_cipher.playfair_decrypt(
            cipher_text,
            playfair_matrix
        )

        return jsonify({
            "decrypted_text": decrypted_text
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Lỗi server",
            "detail": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)