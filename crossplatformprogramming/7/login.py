import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import os
import sys
import subprocess

class Login:
    def __init__(self, appWindow):
        self.appWindow = appWindow
        self.appWindow.title("Sign in")
        self.appWindow.geometry("400x350")
        self.appWindow.resizable(False, False)
        
        self.main_frame = ttk.Frame(appWindow)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(script_dir, "users_file.txt")
        
        self.widgets()
    
    def widgets(self):
        title_label = ttk.Label(
            self.main_frame, 
            text="Sign in",
            font=("Arial", 14)
        )
        title_label.pack(pady=10)
        
        ttk.Label(self.main_frame, text="Username:").pack(anchor=tk.W, pady=10)
        self.in_username = ttk.Entry(self.main_frame, width=30)
        self.in_username.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.main_frame, text="Password:").pack(anchor=tk.W, pady=10)
        self.in_password = ttk.Entry(self.main_frame, width=30, show="*")
        self.in_password.pack(fill=tk.X, pady=5)
        
        login_button = ttk.Button(
            self.main_frame, 
            text="Sign in", 
            command=self.login_user
        )
        login_button.pack(pady=20)

        back_button = ttk.Button(
            self.main_frame, 
            text="Sign up", 
            command=self.redirect_to_signup
        )
        back_button.pack()

    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login_user(self):
        username = self.in_username.get().strip()
        password = self.in_password.get()
        
        if not username:
            messagebox.showerror("Error", "Input username")
            return        
        if not password:
            messagebox.showerror("Error", "Input password")
            return
        
        users_file_path = os.path.abspath(self.users_file)
                
        hashed_password = self.hash_password(password)
        user_found = False
        
        with open(users_file_path, "r") as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    if parts[0] == username and parts[1] == hashed_password:
                        user_found = True
                        break
        
        if user_found:
            messagebox.showinfo("Already", "You`re signed!")
            self.redirect_to_calculator()
        else:
            messagebox.showerror("Error", "Invalid data")

    def redirect_to_calculator(self):
        self.appWindow.destroy()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        calculator_script = os.path.join(script_dir, "credit.py")
                
        if sys.platform == "win32":
            subprocess.Popen([sys.executable, calculator_script])
        else:
            subprocess.Popen(["python3", calculator_script])

    def redirect_to_signup(self):
        self.appWindow.destroy()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        calculator_script = os.path.join(script_dir, "registration.py")
                
        if sys.platform == "win32":
            subprocess.Popen([sys.executable, calculator_script])
        else:
            subprocess.Popen(["python3", calculator_script])

if __name__ == "__main__":
    appWindow = tk.Tk()
    app = Login(appWindow)
    appWindow.mainloop()