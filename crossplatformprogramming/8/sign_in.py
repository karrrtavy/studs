import sys
import os
import hashlib
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import Qt

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sign in')
        self.setFixedSize(400, 350)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(script_dir, 'users_file.txt')
        
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)
        layout.setContentsMargins(30, 20, 30, 20)
        
        title_label = QLabel('Sign in')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 16px; font-weight: bold;')
        layout.addWidget(title_label)
        
        self.username_input = self.create_input_field('Username:', layout)
        self.password_input = self.create_input_field('Password:', layout, is_password=True)
        
        login_btn = QPushButton('Sign in')
        login_btn.setFixedHeight(35)
        login_btn.clicked.connect(self.login_user)
        layout.addWidget(login_btn)
        
        signup_btn = QPushButton('Sign up')
        signup_btn.setFixedHeight(35)
        signup_btn.clicked.connect(self.redirect_to_signup)
        layout.addWidget(signup_btn)
        
        layout.addStretch()
    
    def create_input_field(self, label_text, layout, is_password=False):
        label = QLabel(label_text)
        layout.addWidget(label)
        
        input_field = QLineEdit()
        input_field.setFixedHeight(30)
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(input_field)
        
        return input_field
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login_user(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username:
            QMessageBox.critical(self, 'Error', 'Please enter username')
            return
        if not password:
            QMessageBox.critical(self, 'Error', 'Please enter password')
            return
        
        if not os.path.exists(self.users_file):
            QMessageBox.critical(self, 'Error', 'No registered users found')
            return
        
        hashed_password = self.hash_password(password)
        user_found = False
        
        with open(self.users_file, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2 and parts[0] == username and parts[1] == hashed_password:
                    user_found = True
                    break
        
        if user_found:
            QMessageBox.information(self, 'Success', 'You`re signed')
            self.redirect_to_calculator()
        else:
            QMessageBox.critical(self, 'Error"', 'Invalid username or password')
    
    def redirect_to_calculator(self):
        self.close()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        calculator_script = os.path.join(current_dir, 'credit.py')
        
        subprocess.Popen([sys.executable, calculator_script])
    
    def redirect_to_signup(self):
        self.close()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        signup_script = os.path.join(current_dir, 'sign_up.py')
        
        subprocess.Popen([sys.executable, signup_script])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())