import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Caesar Cipher - Nguyễn Thanh Trung - 2380602369")
        self.ui.pushEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.pushDecrypt.clicked.connect(self.call_api_decrypt)

    def show_success(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.exec_()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Lỗi")
        msg.setText(message)
        msg.exec_()

    def get_error_message(self, response):
        try:
            data = response.json()
            return data.get("error", "Có lỗi xảy ra khi gọi API")
        except Exception:
            return "Có lỗi xảy ra khi gọi API"

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"

        payload = {
            "plain_text": self.ui.textPlainText.toPlainText(),
            "key": self.ui.textKey.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.textCipherText.setText(data["encrypted_text"])
                self.show_success("Mã hóa thành công")
            else:
                error_message = self.get_error_message(response)
                self.show_error(error_message)

        except requests.exceptions.RequestException:
            self.show_error("Không thể kết nối đến API. Hãy kiểm tra xem api.py của Bài 2 đã chạy chưa.")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"

        payload = {
            "cipher_text": self.ui.textCipherText.toPlainText(),
            "key": self.ui.textKey.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.textPlainText.setText(data["decrypted_text"])
                self.show_success("Giải mã thành công")
            else:
                error_message = self.get_error_message(response)
                self.show_error(error_message)

        except requests.exceptions.RequestException:
            self.show_error("Không thể kết nối đến API. Hãy kiểm tra xem api.py của Bài 2 đã chạy chưa.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())