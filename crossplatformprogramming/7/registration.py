# окно авторизации и регистрации, после успешной рег открывается кредитный кальултор, регистрация в отдельной файл

import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import os
import sys
import subprocess

class Registration():
    def __init__(self, appWindow):
        self.appWindow = appWindow
        self.appWindow.title("Sign up")
        self.appWindow.geometry("400x450")
        self.appWindow.resizable(False, False)

        self.main_frame = ttk.Frame(appWindow)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.widgets()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(script_dir, "users_file.txt")

        self.appWindow.mainloop()

    def redirect_to_login(self):
        self.appWindow.destroy()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        login_script = os.path.join(current_dir, "login.py")
        
        if sys.platform == "win32":
            subprocess.Popen([sys.executable, login_script])
        else:
            subprocess.Popen(["python3", login_script])

    def widgets(self):
        title_label = ttk.Label(
            self.main_frame,
            text='Registration',
            font=('Arial', 32)
        )
        title_label.pack(pady=10)

        ttk.Label(self.main_frame, text='Username:').pack(anchor='center', pady=10, )
        self.in_username = ttk.Entry(self.main_frame, width=30)
        self.in_username.pack(pady=5)

        ttk.Label(self.main_frame, text='Password:').pack(anchor='center', pady=10)
        self.in_password = ttk.Entry(self.main_frame, width=30, show='*')
        self.in_password.pack(pady=5)

        ttk.Label(self.main_frame, text='Repeat password:').pack(anchor='center', pady=10)
        self.in_rpassword = ttk.Entry(self.main_frame, width=30, show='*')
        self.in_rpassword.pack(pady=5)

        btn = ttk.Button(
            self.main_frame,
            text='Register',
            command=self.register_user
        )
        btn.pack(pady=20)

        btn2 = ttk.Button(
            self.main_frame,
            text='Sign in',
            command=self.redirect_to_login
        )
        btn2.pack()


    def register_user(self):
        username = self.in_username.get().strip()
        password = self.in_password.get()
        rpassword = self.in_rpassword.get()

        if not username:
            messagebox.showerror('Error', 'Field can`t be empty')
            return
        if not password:
            messagebox.showerror('Error', 'Field can`t be empty')
            return
        if password != rpassword:
            messagebox.showerror('Error', 'Invalid password')
            return
        if self.user_exists(username):
            messagebox.showerror('Error', 'User already exist')
            return

        hashed_password = self.hash_password(password)

        with open(self.users_file, 'a') as f:
            f.write(f'{username}:{hashed_password} \n')

        messagebox.showinfo('Already', 'You`re registered')
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

if __name__ == "__main__":
    appWindow = tk.Tk()
    app = Registration(appWindow)