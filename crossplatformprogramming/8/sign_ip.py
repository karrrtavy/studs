import sys
import os
import hashlib
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign up")
        self.setFixedSize(400, 400)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(script_dir, "users_file.txt")
        
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)
        layout.setContentsMargins(30, 20, 30, 20)
        
        title_label = QLabel("Registration")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title_label)
        
        self.username_input = self.create_input_field("Username:", layout)
        self.password_input = self.create_input_field("Password:", layout, is_password=True)
        self.repeat_password_input = self.create_input_field("Repeat password:", layout, is_password=True)
        
        register_btn = QPushButton("Register")
        register_btn.setFixedHeight(35)
        register_btn.clicked.connect(self.register_user)
        layout.addWidget(register_btn)
        
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
    
    def register_user(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        repeat_password = self.repeat_password_input.text()
        
        if not username:
            QMessageBox.critical(self, "Error", "Username field can't be empty")
            return
        if not password:
            QMessageBox.critical(self, "Error", "Password field can't be empty")
            return
        if password != repeat_password:
            QMessageBox.critical(self, "Error", "Passwords don't match")
            return
        if self.user_exists(username):
            QMessageBox.critical(self, "Error", "User already exists")
            return
        
        hashed_password = self.hash_password(password)
        
        with open(self.users_file, 'a') as f:
            f.write(f"{username}:{hashed_password}\n")
        
        QMessageBox.information(self, "Success", "You are registered successfully!")
        self.redirect_to_login()
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def user_exists(self, username):
        if not os.path.exists(self.users_file):
            return False
        
        with open(self.users_file, 'r') as f:
            for line in f:
                if line.split(':')[0] == username:
                    return True
        return False
    
    def redirect_to_login(self):
        self.close()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        login_script = os.path.join(current_dir, "login.py")
        
        if os.path.exists(login_script):
            if sys.platform == "win32":
                os.system(f'start python "{login_script}"')
            else:
                os.system(f'python3 "{login_script}"')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())