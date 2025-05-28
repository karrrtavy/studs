import tkinter as tk
from tkinter import ttk, messagebox

class CreditCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Кредитный калькулятор")
        self.master.geometry("500x500")
        
        # Основной фрейм с прокруткой
        main_frame = ttk.Frame(master)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Холст и скроллбар для прокрутки
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Создаем элементы интерфейса
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        title_label = ttk.Label(
            self.scrollable_frame, 
            text="Кредитный калькулятор",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=10, anchor="center")
        
        # Фрейм для ввода данных
        input_frame = ttk.LabelFrame(self.scrollable_frame, text="Параметры кредита")
        input_frame.pack(pady=10, fill=tk.X, padx=5)
        
        # Сумма кредита
        ttk.Label(input_frame, text="Сумма кредита (руб):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Процентная ставка
        ttk.Label(input_frame, text="Процентная ставка (% годовых):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rate_entry = ttk.Entry(input_frame, width=15)
        self.rate_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Срок кредита
        ttk.Label(input_frame, text="Срок кредита (месяцев):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.term_entry = ttk.Entry(input_frame, width=15)
        self.term_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Тип платежа
        ttk.Label(input_frame, text="Тип платежа:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.payment_type = tk.StringVar(value="annuity")
        
        payment_frame = ttk.Frame(input_frame)
        payment_frame.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="w")
        
        ttk.Radiobutton(
            payment_frame, 
            text="Аннуитетный (равные платежи)", 
            variable=self.payment_type, 
            value="annuity"
        ).pack(anchor="w")
        
        ttk.Radiobutton(
            payment_frame, 
            text="Дифференцированный (уменьшающиеся платежи)", 
            variable=self.payment_type, 
            value="differentiated"
        ).pack(anchor="w")
        
        # Кнопка расчета
        button_frame = ttk.Frame(self.scrollable_frame)
        button_frame.pack(pady=10)
        
        calculate_button = ttk.Button(
            button_frame, 
            text="Рассчитать", 
            command=self.calculate_payment,
            width=15
        )
        calculate_button.pack()
        
        # Фрейм для результатов
        result_frame = ttk.LabelFrame(self.scrollable_frame, text="Результаты расчета")
        result_frame.pack(pady=10, fill=tk.X, padx=5)
        
        # Поле для результата с прокруткой
        result_text_frame = ttk.Frame(result_frame)
        result_text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(result_text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_text = tk.Text(
            result_text_frame, 
            height=8, 
            width=50,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD,
            font=("Arial", 10)
        )
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_text.yview)
        
        # Вставляем приветственный текст
        self.result_text.insert(tk.END, "Введите параметры кредита и нажмите 'Рассчитать'")
    
    def calculate_payment(self):
        """Расчет кредитных платежей"""
        try:
            amount = float(self.amount_entry.get().replace(",", "."))
            rate = float(self.rate_entry.get().replace(",", ".")) / 100 / 12  # Месячная ставка
            term = int(self.term_entry.get())
            payment_type = self.payment_type.get()
            
            # Проверка на корректные значения
            if amount <= 0 or rate <= 0 or term <= 0:
                raise ValueError("Значения должны быть положительными")
            
            self.result_text.delete(1.0, tk.END)
            
            if payment_type == "annuity":
                # Расчет аннуитетного платежа
                if rate == 0:
                    monthly_payment = amount / term
                else:
                    annuity_ratio = (rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
                    monthly_payment = amount * annuity_ratio
                
                total_payment = monthly_payment * term
                overpayment = total_payment - amount
                
                result = (
                    f"РАСЧЕТ АННУИТЕТНОГО ПЛАТЕЖА\n\n"
                    f"Сумма кредита: {amount:,.2f} ₽\n"
                    f"Процентная ставка: {rate*12*100:.2f}% годовых\n"
                    f"Срок кредита: {term} месяцев\n\n"
                    f"Ежемесячный платеж: {monthly_payment:,.2f} ₽\n"
                    f"Общая сумма выплат: {total_payment:,.2f} ₽\n"
                    f"Переплата по кредиту: {overpayment:,.2f} ₽\n"
                    f"Эффективная ставка: {overpayment/amount*100:.2f}%"
                )
                
                # Добавляем график платежей
                self.result_text.insert(tk.END, result + "\n\n")
                self.result_text.insert(tk.END, "ГРАФИК ПЛАТЕЖЕЙ:\n")
                self.result_text.insert(tk.END, "Месяц | Платеж | Основной долг | Проценты | Остаток\n")
                self.result_text.insert(tk.END, "-"*60 + "\n")
                
                balance = amount
                for month in range(1, term + 1):
                    interest = balance * rate
                    principal = monthly_payment - interest
                    balance -= principal
                    
                    if balance < 0:
                        balance = 0
                    
                    self.result_text.insert(
                        tk.END, 
                        f"{month:5d} | {monthly_payment:7.2f} | {principal:13.2f} | {interest:8.2f} | {balance:10.2f}\n"
                    )
            
            else:
                # Расчет дифференцированного платежа
                principal = amount / term
                payments = []
                total_payment = 0
                balances = []
                
                balance = amount
                for month in range(1, term + 1):
                    interest = balance * rate
                    payment = principal + interest
                    payments.append(payment)
                    total_payment += payment
                    balance -= principal
                    balances.append(balance)
                
                overpayment = total_payment - amount
                
                result = (
                    f"РАСЧЕТ ДИФФЕРЕНЦИРОВАННОГО ПЛАТЕЖА\n\n"
                    f"Сумма кредита: {amount:,.2f} ₽\n"
                    f"Процентная ставка: {rate*12*100:.2f}% годовых\n"
                    f"Срок кредита: {term} месяцев\n\n"
                    f"Первый платеж: {payments[0]:,.2f} ₽\n"
                    f"Последний платеж: {payments[-1]:,.2f} ₽\n"
                    f"Общая сумма выплат: {total_payment:,.2f} ₽\n"
                    f"Переплата по кредиту: {overpayment:,.2f} ₽\n"
                    f"Эффективная ставка: {overpayment/amount*100:.2f}%"
                )
                
                # Добавляем график платежей
                self.result_text.insert(tk.END, result + "\n\n")
                self.result_text.insert(tk.END, "ГРАФИК ПЛАТЕЖЕЙ:\n")
                self.result_text.insert(tk.END, "Месяц |   Платеж   | Основной долг | Проценты |  Остаток\n")
                self.result_text.insert(tk.END, "-"*60 + "\n")
                
                for month in range(term):
                    self.result_text.insert(
                        tk.END, 
                        f"{month+1:5d} | {payments[month]:10.2f} | {principal:13.2f} | "
                        f"{payments[month]-principal:8.2f} | {balances[month]:10.2f}\n"
                    )
            
            # Делаем текст только для чтения после расчета
            self.result_text.config(state=tk.NORMAL)
            
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Некорректные данные: {str(e)}")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Срок кредита не может быть нулевым")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    appWindow = tk.Tk()
    app = CreditCalculator(appWindow)
    appWindow.mainloop()