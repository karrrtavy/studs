import tkinter as tk
from tkinter import messagebox

class PrimeButtonWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно с кнопкой простых чисел")
        
        self.click_count = 0
        self.n = 1  # Начальное значение n для формулы 2^n - 1
        self.primes = []  # Список найденных простых чисел
        
        self.button = tk.Button(
            master, 
            text="Щелкните меня (0)", 
            command=self.update_button_text
        )
        self.button.pack(pady=20)
    
    def is_prime(self, num):
        """Проверяет, является ли число простым"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def update_button_text(self):
        self.click_count += 1
        
        # Находим следующее простое число вида 2^n - 1
        while True:
            candidate = 2**self.n - 1
            if self.is_prime(candidate):
                self.primes.append(candidate)
                self.n += 1
                break
            self.n += 1
        
        self.button.config(
            text=f"Щелчок: {self.click_count}, Число: {self.primes[-1]}"
        )

class StoryWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно с рассказом")
        
        # Первое текстовое поле с началом рассказа
        self.story_part1 = tk.Text(master, height=5, width=50)
        self.story_part1.insert(
            tk.END, 
            "Я ничего умного не придумал\n"
            "На этом все:\n"
            "Введи пароль.'\n"
        )
        self.story_part1.pack(pady=10)
        
        # Поле для ввода пароля
        self.password_label = tk.Label(master)
        self.password_label.pack()
        
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)
        
        # Кнопка для продолжения
        self.continue_button = tk.Button(
            master, 
            text="Продолжить рассказ", 
            command=self.continue_story
        )
        self.continue_button.pack(pady=10)
        
        # Второе текстовое поле для завершения
        self.story_part2 = tk.Text(master, height=5, width=50)
        self.story_part2.pack(pady=10)
    
    def continue_story(self):
        password = self.password_entry.get()
        
        if password == "0705":  
            self.story_part2.delete(1.0, tk.END)
            self.story_part2.insert(
                tk.END,
                "Продолжения не будет\n"
                "Я сказал что все конец\n"
            )
        else:
            self.story_part2.delete(1.0, tk.END)
            self.story_part2.insert(
                tk.END,
                "Даже пароль не знаете\n"
            )

class CheckboxWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно с флажками (буквы)")
        
        self.letters = ['П', 'Р', 'И', 'В', 'ЕТ']  # 5 букв кириллицы
        self.check_vars = []
        
        # Создаем флажки
        for letter in self.letters:
            var = tk.IntVar()
            cb = tk.Checkbutton(
                master, 
                text=f"Буква '{letter}'", 
                variable=var
            )
            cb.pack(anchor=tk.W)
            self.check_vars.append(var)
        
        # Кнопка для составления слова
        self.compose_button = tk.Button(
            master, 
            text="Составить слово", 
            command=self.compose_word
        )
        self.compose_button.pack(pady=10)
        
        # Поле для результата
        self.result_text = tk.Text(master, height=2, width=30)
        self.result_text.pack(pady=10)
    
    def compose_word(self):
        selected_letters = [
            self.letters[i] 
            for i, var in enumerate(self.check_vars) 
            if var.get() == 1
        ]
        word = ''.join(selected_letters)
        
        self.result_text.delete(1.0, tk.END)
        if word:
            self.result_text.insert(tk.END, f"Полученное слово: {word}")
        else:
            self.result_text.insert(tk.END, "Выберите хотя бы одну букву")

class RadioWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно с переключателями (неизменяемые типы)")
        
        # Неизменяемые типы в Python
        self.types = [
            ("Кортеж (tuple)", "(1, 2, 3)"),
            ("Строка (str)", "'Неизменяемая строка'"),
            ("Число (int)", "42"),
            ("Число (float)", "3.14"),
            ("Фрозенсет (frozenset)", "frozenset({1, 2, 3})")
        ]
        
        self.selected_type = tk.StringVar()
        self.selected_type.set(self.types[0][1])  # Устанавливаем значение по умолчанию
        
        # Создаем переключатели
        for text, value in self.types:
            rb = tk.Radiobutton(
                master, 
                text=text, 
                variable=self.selected_type, 
                value=value
            )
            rb.pack(anchor=tk.W)
        
        # Кнопка для отображения результата
        self.show_button = tk.Button(
            master, 
            text="Показать пример", 
            command=self.show_example
        )
        self.show_button.pack(pady=10)
        
        # Поле для результата
        self.result_text = tk.Text(master, height=2, width=30)
        self.result_text.pack(pady=10)
    
    def show_example(self):
        example = self.selected_type.get()
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Пример неизменяемого типа: {example}")

def main():
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry("300x250")
    
    # Создаем кнопки для открытия каждого окна
    btn1 = tk.Button(
        root, 
        text="Окно простых чисел", 
        command=lambda: PrimeButtonWindow(tk.Toplevel(root))
    )
    btn1.pack(pady=5, fill=tk.X, padx=20)
    
    btn2 = tk.Button(
        root, 
        text="Окно с рассказом", 
        command=lambda: StoryWindow(tk.Toplevel(root))
    )
    btn2.pack(pady=5, fill=tk.X, padx=20)
    
    btn3 = tk.Button(
        root, 
        text="Окно с буквами", 
        command=lambda: CheckboxWindow(tk.Toplevel(root))
    )
    btn3.pack(pady=5, fill=tk.X, padx=20)
    
    btn4 = tk.Button(
        root, 
        text="Окно с типами данных", 
        command=lambda: RadioWindow(tk.Toplevel(root))
    )
    btn4.pack(pady=5, fill=tk.X, padx=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()