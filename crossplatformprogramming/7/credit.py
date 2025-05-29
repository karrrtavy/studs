import tkinter as tk
from tkinter import ttk, messagebox

class CreditCalculator:
    def __init__(self, appWindow):
        self.appWindow = appWindow
        self.appWindow.title("Credit Calculator")
        self.appWindow.geometry("500x600")
        
        main_frame = ttk.Frame(appWindow)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.widgets(main_frame)
    
    def widgets(self, parent):
        title_label = ttk.Label(
            parent, 
            text="Credit Calculator",
            font=("Arial", 14)
        )
        title_label.pack(pady=10)
        
        input_frame = ttk.LabelFrame(parent, text="Credit settings")
        input_frame.pack(fill=tk.X, pady=8)
        
        ttk.Label(input_frame, text="Cash (rub):").pack(anchor=tk.W, pady=5)
        self.amount_entry = ttk.Entry(input_frame)
        self.amount_entry.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Interest rate (% years):").pack(anchor=tk.W, pady=5)
        self.rate_entry = ttk.Entry(input_frame)
        self.rate_entry.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Period (month):").pack(anchor=tk.W, pady=5)
        self.term_entry = ttk.Entry(input_frame)
        self.term_entry.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Type:").pack(anchor=tk.W, pady=5)
        self.payment_type = tk.StringVar(value="annuity")
        
        payment_frame = ttk.Frame(input_frame)
        payment_frame.pack(anchor=tk.W, pady=5)
        
        calculate_button = ttk.Button(
            parent, 
            text="Calculate", 
            command=self.calculate_payment
        )
        calculate_button.pack(expand=True, pady=10)
        
        result_frame = ttk.LabelFrame(parent, text='Result')
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = tk.Text(
            result_frame, 
            height=15,
            wrap=tk.WORD,
            font=("Arial", 10)
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
    def calculate_payment(self):
        try:
            amount = float(self.amount_entry.get())
            annual_rate = float(self.rate_entry.get())
            monthly_rate = annual_rate / 100 / 12
            term = int(self.term_entry.get())
            
            if amount <= 0 or annual_rate <= 0 or term <= 0:
                raise ValueError("Values must be positive")
            
            self.result_text.delete(1.0, tk.END)
            
            if monthly_rate == 0:
                monthly_payment = amount / term
            else:
                annuity_ratio = (monthly_rate * (1 + monthly_rate) ** term) / ((1 + monthly_rate) ** term - 1)
                monthly_payment = amount * annuity_ratio
            
            total_payment = monthly_payment * term
            overpayment = total_payment - amount
            
            result = (
                f"Amount: {amount:,.2f} \n"
                f"Interest rate: {annual_rate:.2f}% per year\n"
                f"Term: {term} months\n\n"
                f"Monthly payment: {monthly_payment:,.2f} \n"
                f"Total payment: {total_payment:,.2f} \n"
                f"Overpayment: {overpayment:,.2f} \n\n"
            )
            
            self.result_text.insert(tk.END, result)
            
            balance = amount
            for month in range(1, term + 1):
                interest = balance * monthly_rate
                principal = monthly_payment - interest
                balance -= principal
                
                if balance < 0.01:
                    balance = 0
                                        
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid data: {str(e)}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Term can`t be zero")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    appWindow = tk.Tk()
    app = CreditCalculator(appWindow)
    appWindow.mainloop()