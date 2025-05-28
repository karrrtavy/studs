import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import os
import sys
import subprocess

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Вход в систему")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        
        # Основной фрейм
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Определяем путь к файлу пользователей относительно расположения этого скрипта
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(script_dir, "..", "7", "users_file.txt")
        
        # Создаем элементы интерфейса
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        title_label = ttk.Label(
            self.main_frame, 
            text="Вход в систему",
            font=("Arial", 14)
        )
        title_label.pack(pady=10)
        
        # Поле для имени пользователя
        ttk.Label(self.main_frame, text="Имя пользователя:").pack(anchor=tk.W, pady=(10, 0))
        self.username_entry = ttk.Entry(self.main_frame, width=30)
        self.username_entry.pack(fill=tk.X, pady=5)
        
        # Поле для пароля
        ttk.Label(self.main_frame, text="Пароль:").pack(anchor=tk.W, pady=(10, 0))
        self.password_entry = ttk.Entry(self.main_frame, width=30, show="*")
        self.password_entry.pack(fill=tk.X, pady=5)
        
        # Кнопка входа
        login_button = ttk.Button(
            self.main_frame, 
            text="Войти", 
            command=self.login_user
        )
        login_button.pack(pady=20)
    
    def hash_password(self, password):
        """Хэширование пароля с использованием SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login_user(self):
        """Обработка входа пользователя"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Проверка введенных данных
        if not username:
            messagebox.showerror("Ошибка", "Введите имя пользователя")
            return
        
        if not password:
            messagebox.showerror("Ошибка", "Введите пароль")
            return
        
        # Получаем абсолютный путь к файлу
        users_file_path = os.path.abspath(self.users_file)
        
        # Проверка существования файла с пользователями
        if not os.path.exists(users_file_path):
            messagebox.showerror("Ошибка", f"База пользователей не найдена по пути: {users_file_path}")
            return
        
        # Поиск пользователя в базе
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
            messagebox.showinfo("Успех", "Вход выполнен успешно!")
            self.redirect_to_calculator()
            # Здесь можно добавить переход к основному функционалу приложения
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")

    def redirect_to_calculator(self):
        """Перенаправление на кредитный калькулятор"""
        self.master.destroy()
        
        # Определяем путь к скрипту калькулятора (в той же папке)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        calculator_script = os.path.join(script_dir, "credit.py")
        
        # Проверяем существование файла
        if not os.path.exists(calculator_script):
            messagebox.showerror("Ошибка", f"Файл калькулятора не найден: {calculator_script}")
            return
        
        # Запускаем скрипт калькулятора
        if sys.platform == "win32":
            subprocess.Popen([sys.executable, calculator_script])
        else:
            subprocess.Popen(["python3", calculator_script])

if __name__ == "__main__":
    appWindow = tk.Tk()
    app = Login(appWindow)
    appWindow.mainloop()