import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class RSA_Cipher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)
        
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5500/api/rsa/generate_keys"
        try:
            response = requests.post(url)
            if response.status_code == 200:
                data = response.json()
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5500/api/rsa/encrypt"
        payload = {
            "message" : self.ui.txt_plain_text.toPlainText(),
            "key_type" : "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setText("Encryption Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5500/api/rsa/decrypt"
        payload = {
            "message" : self.ui.txt_cipher_text.toPlainText(),
            "key_type" : "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setText("Decryption Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_sign(self):
        url = "http://127.0.0.1:5500/api/rsa/sign"
        payload = {
            "message" : self.ui.txt_info.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setText("Signing Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
        
    def call_api_verify(self):
        url = "http://127.0.0.1:5500/api/rsa/verify"
        payload = {
            "message" : self.ui.txt_info.toPlainText(),
            "signature" : self.ui.txt_sign.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_Verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.warning)
                    msg.setText("Verified Fail")
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSA_Cipher()
    window.show()
    sys.exit(app.exec_())

