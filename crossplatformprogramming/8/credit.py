import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGroupBox, QRadioButton,
                             QTextEdit, QMessageBox, QButtonGroup)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CreditCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Credit Calculator')
        self.setFixedSize(500, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # Заголовок
        title_label = QLabel('Credit Calculator')
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Группа настроек кредита
        settings_group = QGroupBox('Credit settings')
        settings_layout = QVBoxLayout(settings_group)
        
        # Поля ввода
        self.amount_entry = self.create_input_field('Cash (rub):', settings_layout)
        self.rate_entry = self.create_input_field('Interest rate (% years):', settings_layout)
        self.term_entry = self.create_input_field('Period (month):', settings_layout)
                
        self.payment_type = QButtonGroup(self)
        
        main_layout.addWidget(settings_group)
        
        self.calculate_btn = QPushButton('Calculate')
        self.calculate_btn.setFixedHeight(40)
        self.calculate_btn.clicked.connect(self.calculate_payment)
        main_layout.addWidget(self.calculate_btn)
        
        result_group = QGroupBox('Result')
        result_layout = QVBoxLayout(result_group)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont('Arial', 10))
        result_layout.addWidget(self.result_text)
        
        main_layout.addWidget(result_group, 1)
    
    def create_input_field(self, label_text, layout):
        hbox = QHBoxLayout()
        label = QLabel(label_text)
        label.setFixedWidth(150)
        hbox.addWidget(label)
        
        input_field = QLineEdit()
        hbox.addWidget(input_field)
        
        layout.addLayout(hbox)
        return input_field
    
    def calculate_payment(self):
        try:
            amount = float(self.amount_entry.text().replace(",", "."))
            annual_rate = float(self.rate_entry.text().replace(",", "."))
            term = int(self.term_entry.text())
            
            if amount <= 0 or annual_rate <= 0 or term <= 0:
                raise ValueError('Values must be positive')
            
            monthly_rate = annual_rate / 100 / 12
            
            self.result_text.clear()
            
            if monthly_rate == 0:
                monthly_payment = amount / term
            else:
                annuity_ratio = (monthly_rate * (1 + monthly_rate) ** term) / ((1 + monthly_rate) ** term - 1)
                monthly_payment = amount * annuity_ratio
            
            total_payment = monthly_payment * term
            overpayment = total_payment - amount
            
            result = (
                f'Amount: {amount:,.2f} RUB<br>'
                f'Interest rate: {annual_rate:.2f}% per year<br>'
                f'Term: {term} months<br><br>'
                f'Monthly payment: <b>{monthly_payment:,.2f} RUB</b><br>'
                f'Total payment: <b>{total_payment:,.2f} RUB</b><br>'
                f'Overpayment: <b>{overpayment:,.2f} RUB</b><br><br>'
            )
                                    
            result += '</table>'
            
            self.result_text.setHtml(result)
                        
        except ValueError as e:
            QMessageBox.critical(self, 'Error', f'Invalid data: {str(e)}')
        except ZeroDivisionError:
            QMessageBox.critical(self, 'Error', 'Term cannot be zero')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    if sys.platform == 'win32':
        import os
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
            os.path.dirname(sys.executable), 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins'
        )
    
    window = CreditCalculator()
    window.show()
    sys.exit(app.exec_())