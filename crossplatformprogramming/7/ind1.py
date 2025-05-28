import tkinter as tk
from tkinter import ttk

class PrimeButtonTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.click_count = 0
        self.n = 1
        self.primes = []
        
        self.button = tk.Button(
            self, 
            text="Click me (0)", 
            command=self.update_button_text
        )
        self.button.pack(pady=20)
    
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def update_button_text(self):
        self.click_count += 1
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

class StoryTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.story_part1 = tk.Text(self, height=5, width=50)
        self.story_part1.insert(
            tk.END, 
            "Я ничего умного не придумал\n"
            "На этом все:\n"
            "Введи пароль.'\n"
        )
        self.story_part1.pack(pady=10)
        
        self.password_label = tk.Label(self)
        self.password_label.pack()
        
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        self.continue_button = tk.Button(
            self, 
            text="Продолжить рассказ", 
            command=self.continue_story
        )
        self.continue_button.pack(pady=10)
        
        self.story_part2 = tk.Text(self, height=5, width=50)
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

class CheckboxTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.letters = ['П', 'Р', 'И', 'В', 'ЕТ']
        self.check_vars = []
        
        for letter in self.letters:
            var = tk.IntVar()
            cb = tk.Checkbutton(
                self, 
                text=f"Буква '{letter}'", 
                variable=var
            )
            cb.pack(anchor=tk.W)
            self.check_vars.append(var)
        
        self.compose_button = tk.Button(
            self, 
            text="Составить слово", 
            command=self.compose_word
        )
        self.compose_button.pack(pady=10)
        
        self.result_text = tk.Text(self, height=2, width=30)
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

class RadioTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.types = [
            ("Кортеж (tuple)", "(1, 2, 3)"),
            ("Строка (str)", "'Неизменяемая строка'"),
            ("Число (int)", "42"),
            ("Число (float)", "3.14"),
            ("Фрозенсет (frozenset)", "frozenset({1, 2, 3})")
        ]
        
        self.selected_type = tk.StringVar()
        self.selected_type.set(self.types[0][1])
        
        for text, value in self.types:
            rb = tk.Radiobutton(
                self, 
                text=text, 
                variable=self.selected_type, 
                value=value
            )
            rb.pack(anchor=tk.W)
        
        self.show_button = tk.Button(
            self, 
            text="Показать пример", 
            command=self.show_example
        )
        self.show_button.pack(pady=10)
        
        self.result_text = tk.Text(self, height=2, width=30)
        self.result_text.pack(pady=10)
    
    def show_example(self):
        example = self.selected_type.get()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Пример неизменяемого типа: {example}")

def main():
    root = tk.Tk()
    root.title("Программа с вкладками")
    root.geometry("500x400")
    
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)
    
    # Создаем вкладки
    tab1 = PrimeButtonTab(notebook)
    notebook.add(tab1, text="Простые числа")
    
    tab2 = StoryTab(notebook)
    notebook.add(tab2, text="Рассказ")
    
    tab3 = CheckboxTab(notebook)
    notebook.add(tab3, text="Буквы")
    
    tab4 = RadioTab(notebook)
    notebook.add(tab4, text="Типы данных")
    
    root.mainloop()

if __name__ == "__main__":
    main()