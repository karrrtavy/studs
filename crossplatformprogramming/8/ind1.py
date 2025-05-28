import tkinter as tk
from tkinter import ttk, messagebox
import hashlib

class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система авторизации")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Стилизация
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TEntry', font=('Arial', 10), padding=5)
        
        # "База данных" пользователей (логин: хеш пароля)
        self.users = {
            'admin': self._hash_password('admin123'),
            'user': self._hash_password('user123')
        }
        
        self.show_login_frame()

    def _hash_password(self, password):
        """Хеширование пароля"""
        return hashlib.sha256(password.encode()).hexdigest()

    def show_login_frame(self):
        """Показывает форму входа"""
        self.clear_window()
        
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(self.login_frame, text="Вход в систему", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Поле логина
        ttk.Label(self.login_frame, text="Логин:").pack()
        self.login_entry = ttk.Entry(self.login_frame)
        self.login_entry.pack(pady=5, fill=tk.X)
        
        # Поле пароля
        ttk.Label(self.login_frame, text="Пароль:").pack()
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5, fill=tk.X)
        
        # Кнопки
        btn_frame = ttk.Frame(self.login_frame)
        btn_frame.pack(pady=10, fill=tk.X)
        
        ttk.Button(btn_frame, text="Войти", command=self.login).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Регистрация", command=self.show_register_frame).pack(side=tk.LEFT, padx=5)

    def show_register_frame(self):
        """Показывает форму регистрации"""
        self.clear_window()
        
        self.register_frame = ttk.Frame(self.root)
        self.register_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(self.register_frame, text="Регистрация", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Поля для регистрации
        fields = [
            ("Логин:", "new_login_entry"),
            ("Пароль:", "new_password_entry"),
            ("Повторите пароль:", "confirm_password_entry")
        ]
        
        self.register_entries = {}
        for text, name in fields:
            ttk.Label(self.register_frame, text=text).pack()
            entry = ttk.Entry(self.register_frame, show="*" if "пароль" in text.lower() else "")
            entry.pack(pady=5, fill=tk.X)
            self.register_entries[name] = entry
        
        # Кнопки
        btn_frame = ttk.Frame(self.register_frame)
        btn_frame.pack(pady=10, fill=tk.X)
        
        ttk.Button(btn_frame, text="Зарегистрироваться", command=self.register).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Назад", command=self.show_login_frame).pack(side=tk.LEFT, padx=5)

    def show_success_frame(self, username):
        """Показывает окно успешной авторизации"""
        self.clear_window()
        
        self.success_frame = ttk.Frame(self.root)
        self.success_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(
            self.success_frame, 
            text=f"Добро пожаловать, {username}!",
            font=('Arial', 14, 'bold')
        ).pack(pady=20)
        
        ttk.Label(
            self.success_frame, 
            text="Вы успешно авторизовались в системе",
            font=('Arial', 10)
        ).pack(pady=10)
        
        # Имитация контента для авторизованного пользователя
        content_frame = ttk.Frame(self.success_frame)
        content_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(content_frame, text="Ваши последние действия:").pack()
        ttk.Label(content_frame, text="- Вход в систему: только что").pack(pady=5)
        ttk.Label(content_frame, text="- Последний вход: сегодня").pack(pady=5)
        
        ttk.Button(
            self.success_frame, 
            text="Выйти", 
            command=self.show_login_frame
        ).pack(pady=20)

    def clear_window(self):
        """Очищает окно от всех виджетов"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        """Обработка входа"""
        username = self.login_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены")
            return
        
        if username in self.users:
            if self.users[username] == self._hash_password(password):
                self.show_success_frame(username)
                return
        
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def register(self):
        """Обработка регистрации"""
        username = self.register_entries['new_login_entry'].get()
        password = self.register_entries['new_password_entry'].get()
        confirm = self.register_entries['confirm_password_entry'].get()
        
        if not all([username, password, confirm]):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены")
            return
        
        if password != confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают")
            return
        
        if username in self.users:
            messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует")
            return
        
        if len(password) < 6:
            messagebox.showerror("Ошибка", "Пароль должен содержать минимум 6 символов")
            return
        
        # Регистрируем нового пользователя
        self.users[username] = self._hash_password(password)
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.show_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()