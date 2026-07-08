# -*- coding: utf-8 -*-
import sys
import json
from datetime import datetime
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QMessageBox, QInputDialog, QListWidgetItem
from destipcal import Ui_MainWindow
from database import DatabaseManager
from data_io import export_to_json, import_from_json
from image_generator import generate_receipt_image
import sqlite3

class Mywin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = DatabaseManager()

        self.ui.pushButtoncalculate.clicked.connect(self.calculate_tip)
        self.ui.pushButtonreset.clicked.connect(self.reset_fields)
        self.ui.pushButtonHistory.clicked.connect(self.show_history_dialog)
        
        self._setup_additional_actions()

    def _setup_additional_actions(self):
        if not hasattr(self.ui, 'pushButtonExport'):
            self.ui.pushButtonExport = QtWidgets.QPushButton("Экспорт", self.ui.centralwidget)
            self.ui.gridLayout.addWidget(self.ui.pushButtonExport, 7, 0, 1, 2)
        self.ui.pushButtonExport.clicked.connect(self.export_data)

        if not hasattr(self.ui, 'pushButtonImport'):
            self.ui.pushButtonImport = QtWidgets.QPushButton("Импорт", self.ui.centralwidget)
            self.ui.gridLayout.addWidget(self.ui.pushButtonImport, 8, 0, 1, 2)
        self.ui.pushButtonImport.clicked.connect(self.import_data)

    def calculate_tip(self):
        try:
            bill_amount = self.ui.doubleSpinBoxbill.value()
            tip_percent_str = self.ui.comboBoxtipprecent.currentText().replace('%', '')
            tip_percent = float(tip_percent_str) / 100
            
            people_count = int(self.ui.comboBoxpeople.currentText())
            tax_percent_decimal = self.ui.doubleSpinBoxtax.value() / 100

            tax_amount = bill_amount * tax_percent_decimal
            subtotal = bill_amount + tax_amount
            tip_amount = subtotal * tip_percent
            total_sum = subtotal + tip_amount
            per_person = total_sum / people_count

            rounded_total = round(total_sum, 2)
            rounded_per_person = round(per_person, 2)

            self.ui.labelresultperpersonnumber.setText(f"{rounded_per_person:,.2f} руб.".replace(',', 'X').replace('.', ',').replace('X', '.'))
            self.ui.labelresulttotalnumber.setText(f"{rounded_total:,.2f} руб.".replace(',', 'X').replace('.', ',').replace('X', '.'))

            calc_id = self.db.save_calculation((
                bill_amount, 
                tax_percent_decimal * 100,
                tip_percent * 100,
                people_count, 
                rounded_total, 
                rounded_per_person,
                datetime.now().isoformat()
            ))
            
            img_path = f"receipt_{calc_id}.png"
            generate_receipt_image(
                bill=bill_amount, 
                tax=tax_percent_decimal * 100, 
                tip=tip_percent * 100, 
                people=people_count, 
                total=rounded_total, 
                path=img_path
            )
            print(f"Чек сохранен как {img_path}")

        except Exception as e:
            print(f"Ошибка расчета: {e}")
            QMessageBox.warning(self, "Ошибка", f"ошибка в расчете:\n{e}")

    def reset_fields(self):
        self.ui.doubleSpinBoxbill.setValue(0.01)
        self.ui.comboBoxtipprecent.setCurrentText("15%")
        self.ui.comboBoxpeople.setCurrentText("1")
        self.ui.doubleSpinBoxtax.setValue(0.0)
        self.ui.labelresultperpersonnumber.setText("0,00 руб.")
        self.ui.labelresulttotalnumber.setText("0,00 руб.")

    def show_history_dialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("История расчетов")
        dialog.resize(500, 400)
        
        layout = QtWidgets.QVBoxLayout(dialog)
        
        list_widget = QtWidgets.QListWidget()
        history = self.db.get_all_calculations()
        
        for row in history:
            item_text = (
                f"[{datetime.fromisoformat(row[7]).strftime('%d.%m %H:%M')}] "
                f"Счет: {row[1]:.2f} ₽ | Налог: {row[2]}% | Чаевые: {row[3]}% | Гости: {row[4]}\n"
                f"Итого: {row[5]:.2f} ₽ ({row[6]:.2f} ₽/чел)"
            )
            item = QListWidgetItem(item_text)
            item.setData(QtCore.Qt.ItemDataRole.UserRole, row[0])
            list_widget.addItem(item)
            
        layout.addWidget(list_widget)

        btn_layout = QtWidgets.QHBoxLayout()
        
        btn_delete = QtWidgets.QPushButton("Удалить выбранное")
        btn_delete.clicked.connect(lambda: self._delete_selected_item(list_widget, dialog))
        btn_layout.addWidget(btn_delete)
        
        btn_export_csv = QtWidgets.QPushButton("Экспорт текущей выборки (CSV)")
        btn_export_csv.clicked.connect(lambda: self._export_current_list(history))
        btn_layout.addWidget(btn_export_csv)
        
        layout.addLayout(btn_layout)
        dialog.exec()

    def _delete_selected_item(self, list_widget, dialog):
        selected_items = list_widget.selectedItems()
        if not selected_items:
            return
        
        reply = QMessageBox.question(
            self, 'Подтверждение', 
            'Удалить эту запись из истории?', 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            for item in selected_items:
                calc_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
                self.db.delete_calculation(calc_id) # CRUD - Delete
            dialog.accept()

    def _export_current_list(self, full_history):
        from data_io import export_to_csv
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить CSV", "", "CSV Files (*.csv)")
        if filename:
            export_to_csv(full_history, filename)

    def export_data(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Экспортировать данные", "", "JSON Files (*.json)")
        if filename:
            success = export_to_json(self.db.get_all_calculations(), filename)
            if success:
                QMessageBox.information(self, "Успех", "Данные успешно экспортированы в JSON.")

    def import_data(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Импортировать данные", "", "JSON Files (*.json)")
        if filename:
            imported_data = import_from_json(filename)
            if imported_data is None:
                return
            
            count = 0
            for record in imported_data:
                if len(record) >= 8:
                    try:
                        self.db.save_calculation(tuple(record[1:8]) + (record[7],))
                        count += 1
                    except sqlite3.IntegrityError:
                        pass
            
            QMessageBox.information(self, "Успех", f"Успешно импортировано {count} записей.")

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    font = QtGui.QFont("Times New Roman", 14)
    app.setFont(font)
    
    myapp = Mywin()
    myapp.show()
    sys.exit(app.exec())