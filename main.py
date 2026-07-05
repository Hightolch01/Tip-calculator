import sys
from PySide6 import QtWidgets
from destipcal import Ui_MainWindow



class Mywin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtoncalculate.clicked.connect(self.calculate_tip)
        self.ui.pushButtonreset.clicked.connect(self.reset_fields)

    def calculate_tip(self):
        try:
            bill_amount = self.ui.doubleSpinBoxbill.value() #Сумма
            tip_percent_str = self.ui.comboBoxtipprecent.currentText().replace('%', '')
            tip_percent = float(tip_percent_str) / 100
            
            people_count = int(self.ui.comboBoxpeople.currentText()) #Количество гостей
            tax_percent = self.ui.doubleSpinBoxtax.value() / 100 #Налог

            tax_amount = bill_amount * tax_percent
            subtotal = bill_amount + tax_amount
            tip_amount = subtotal * tip_percent
            total_sum = subtotal + tip_amount
            per_person = total_sum / people_count

            self.ui.labelresultperpersonnumber.setText(f"{per_person:,.2f} руб.".replace(',', 'X').replace('.', ',').replace('X', '.'))
            self.ui.labelresulttotalnumber.setText(f"{total_sum:,.2f} руб.".replace(',', 'X').replace('.', ',').replace('X', '.'))

        except Exception as e:
            print(f"Ошибка расчета: {e}")

    def reset_fields(self):
        self.ui.doubleSpinBoxbill.setValue(0.01)
        self.ui.comboBoxtipprecent.setCurrentText("15%")
        self.ui.comboBoxpeople.setCurrentText("1")
        self.ui.doubleSpinBoxtax.setValue(0.0)
        self.ui.labelresultperpersonnumber.setText("0,00 руб.")
        self.ui.labelresulttotalnumber.setText("0,00 руб.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Mywin()
    myapp.show()
    sys.exit(app.exec())