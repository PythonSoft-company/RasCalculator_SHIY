from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QMessageBox, QTabWidget
import sys
from PyQt6.QtGui import QIcon, QTextCursor
from PyQt6.QtCore import QSize, Qt

class Calculator(QWidget):
	def __init__(self):
		super().__init__()
		
		label_basic_calc_text = QLabel(self)
		label_basic_calc_text.setText("Введите числовое выражение (2+2):")
		label_basic_calc_text.move(0, 0)
		
		self.entry = QLineEdit(self)
		self.entry.move(0, 20)
		
		self.button_calc = QPushButton(self)
		
		self.button_calc.setText("Вычислить")
		self.button_calc.move(216, 15)
		
		self.label = QLabel(self)
		self.label.move(0, 40)
		self.label.resize(1000, 16)
		
		self.button_cor = QPushButton(self, text='√')
		self.button_cor.move(296, 15)
		
class EqualationUI(QWidget):
	def __init__(self):
		super().__init__()
		
		label_system_of_equations_text = QLabel(self, text="Введите систему уравнений (через пробел):")
		label_system_of_equations_text.move(0, 60)
		
		self.entry_system_of_equations = QLineEdit(self)
		self.entry_system_of_equations.move(0, 80)
		
		self.button_system_of_equations = QPushButton(self, text="Решить систему уравнений")
		self.button_system_of_equations.move(305, 80)
		self.entry_system_of_equations.resize(250, 20)
		
		self.label_system_of_equations = QLabel(self)
		self.label_system_of_equations.move(0, 105)
		self.label_system_of_equations.resize(1000, 40)
	
class StatisticUI(QWidget):
	def __init__(self):
		super().__init__()
		
		label_number_entry = QLabel(self, text="Введите числа через пробел:")
		label_number_entry.move(0, 145)
		
		self.entry_numbers = QLineEdit(self)
		self.entry_numbers.resize(245, 20)
		self.entry_numbers.move(0, 165)
		
		self.button_mean = QPushButton(self, text="Среднее значение")
		self.button_mean.move(305, 160)
		
		self.button_median = QPushButton(self, text="Медиана")
		self.button_median.move(418, 160)
		
		self.button_max = QPushButton(self, text="Максимум")
		self.button_max.move(484, 160)
		
		self.button_min = QPushButton(self, text="Минимум")
		self.button_min.move(556, 160)
		
		self.button_range = QPushButton(self, text="Размах")
		self.button_range.move(624, 160)
		
		self.button_variance = QPushButton(self, text="Дисперсия")
		self.button_variance.move(690, 160)
		
		self.label_stat_result = QLabel(self)
		self.label_stat_result.move(0, 200)
		self.label_stat_result.resize(1000, 30)
		
		
class TrigonometryUI(QWidget):
	def __init__(self):
		super().__init__()
		
		cord_x = 0
		cord_y = 220
		self.label_trig_text = QLabel(self, text="Введите угол синус, косинус или тангенс которого вы хотите найти:")
		self.label_trig_text.move(cord_x, cord_y)
		
		self.trig_input = QLineEdit(self)
		self.trig_input.move(cord_x, cord_y + 20)
		
		self.sin_button = QPushButton(self, text="sin")
		self.sin_button.move(cord_x, cord_y + 40)
		
		self.cos_button = QPushButton(self, text="cos")
		self.cos_button.move(cord_x + 100, cord_y + 40)
		
		self.tan_button = QPushButton(self, text="tan")
		self.tan_button.move(cord_x + 200, cord_y + 40)
		
		self.trig_output = QLabel(self)
		self.trig_output.move(cord_x + 135, cord_y + 20)
		self.trig_output.resize(1000, 30)
		
class FractionUI(QWidget):
	def __init__(self):
		super().__init__()
		
		label_fractions_text = QLabel(self, text="Арифметика дробей:")
		label_fractions_text.move(0, 290)
		
		self.entry_first_fraction = QLineEdit(self)
		self.entry_first_fraction.move(0, 310)
		
		self.entry_second_fraction = QLineEdit(self)
		self.entry_second_fraction.move(185, 310)
		
		self.operator_variable = QComboBox(self)
		self.operator_variable.addItems(["+", "-", "*", "/"])
		self.operator_variable.move(125, 310)
		
		self.button_fractions_calculate = QPushButton(self, text="Выполнить операцию")
		self.button_fractions_calculate.move(0, 338)
		
		self.label_fractions_result = QLabel(self)
		self.label_fractions_result.move(0, 363)
		self.label_fractions_result.resize(1000, 20)
		
class HistoryandError(QWidget):
	def __init__(self):
		super().__init__()
		self.error_text = QTextEdit(self)
		self.error_text.setReadOnly(True)
		self.error_text.resize(500, 150)
		self.error_text.move(0, 400)
		self.history_text = QTextEdit(self)
		self.history_text.move(0, 540)
		self.history_text.resize(600, 150)
		self.label_of_errors = QLabel(self, text='Поле с ошибками при вычислении:')
		self.label_of_errors.move(0, 380)
		self.cl_b = QPushButton(self, text="Очистить историю")
		self.cl_b.move(680, 530)
		self.button_exit = QPushButton(self, text="Выход")
		self.button_exit.move(930, 85)
		self.tgb = QPushButton(self, text='Перейти в официальный тгк Калькулятора')
		self.tgb.move(750, 115)
		
		self.form_btn = QPushButton(self, text='Собщить об ошибке')
		self.form_btn.move(870, 150)




class Main(QWidget):
	def __init__(self):
		super().__init__()
		calculator = Calculator()
		calculator.show()
class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		
		# Настройка окна
		self.setWindowTitle("Расширенный калькулятор")
		self.resize(1000, 1000)
		# Кнопка внутри окна
		self.msg_box = QMessageBox(self)
		self.button_settings = QPushButton(self)
		icon = QIcon("settings_icon.png")
		self.button_settings.setIcon(icon)
		self.button_settings.setIconSize(icon.actualSize(QSize(30, 30)))
		self.button_settings.move(955, 0)
		
		label_basic_calc_text = QLabel(self)
		label_basic_calc_text.setText("Введите числовое выражение (2+2):")
		label_basic_calc_text.move(0, 0)
		
		self.help_button = QPushButton(self)
		self.help_button.setText("Справка")
		self.help_button.move(930, 55)
		
		self.entry = QLineEdit(self)
		self.entry.move(0, 20)
		
		self.button_calc = QPushButton(self)
		
		self.button_calc.setText("Вычислить")
		self.button_calc.move(216, 15)
		
		self.label = QLabel(self)
		self.label.move(0, 40)
		self.label.resize(1000, 16)
		label_system_of_equations_text = QLabel(self, text="Введите систему уравнений (через пробел):")
		label_system_of_equations_text.move(0, 60)
		
		self.entry_system_of_equations = QLineEdit(self)
		self.entry_system_of_equations.move(0, 80)
		
		self.button_system_of_equations = QPushButton(self, text="Решить систему уравнений")
		self.button_system_of_equations.move(305, 80)
		self.entry_system_of_equations.resize(250, 20)
		
		self.label_system_of_equations = QLabel(self)
		self.label_system_of_equations.move(0, 105)
		self.label_system_of_equations.resize(1000, 40)
		label_number_entry = QLabel(self, text="Введите числа через пробел:")
		label_number_entry.move(0, 145)
		
		self.entry_numbers = QLineEdit(self)
		self.entry_numbers.resize(245, 20)
		self.entry_numbers.move(0, 165)
		
		self.button_mean = QPushButton(self, text="Среднее значение")
		self.button_mean.move(305, 160)
		
		self.button_median = QPushButton(self, text="Медиана")
		self.button_median.move(418, 160)
		
		self.button_max = QPushButton(self, text="Максимум")
		self.button_max.move(484, 160)
		
		self.button_min = QPushButton(self, text="Минимум")
		self.button_min.move(556, 160)
		
		self.button_range = QPushButton(self, text="Размах")
		self.button_range.move(624, 160)
		
		self.button_variance = QPushButton(self, text="Дисперсия")
		self.button_variance.move(690, 160)
		
		self.label_stat_result = QLabel(self)
		self.label_stat_result.move(0, 200)
		self.label_stat_result.resize(1000, 30)
		self.button_exit = QPushButton(self, text="Выход")
		self.button_exit.move(930, 85)
		
		self.error_text = QTextEdit(self)
		self.error_text.setReadOnly(True)
		self.error_text.resize(500, 150)
		self.error_text.move(0, 400)
		
		self.button_cor = QPushButton(self, text='√')
		self.button_cor.move(296, 15)
		label_fractions_text = QLabel(self, text="Арифметика дробей:")
		label_fractions_text.move(0, 290)
		
		self.entry_first_fraction = QLineEdit(self)
		self.entry_first_fraction.move(0, 310)
		
		self.entry_second_fraction = QLineEdit(self)
		self.entry_second_fraction.move(185, 310)
		
		self.operator_variable = QComboBox(self)
		self.operator_variable.addItems(["+", "-", "*", "/"])
		self.operator_variable.move(125, 310)
		
		self.button_fractions_calculate = QPushButton(self, text="Выполнить операцию")
		self.button_fractions_calculate.move(0, 338)
		
		self.label_fractions_result = QLabel(self)
		self.label_fractions_result.move(0, 363)
		self.label_fractions_result.resize(1000, 20)
		self.history_text = QTextEdit(self)
		self.history_text.move(0, 540)
		self.history_text.resize(600, 150)
		self.label_of_errors = QLabel(self, text='Поле с ошибками при вычислении:')
		self.label_of_errors.move(0, 380)
		
		self.cl_b = QPushButton(self, text="Очистить историю")
		self.cl_b.move(680, 530)
		cord_x = 0
		cord_y = 220
		self.label_trig_text = QLabel(self, text="Введите угол синус, косинус или тангенс которого вы хотите найти:")
		self.label_trig_text.move(cord_x, cord_y)
		
		self.trig_input = QLineEdit(self)
		self.trig_input.move(cord_x, cord_y + 20)
		
		self.sin_button = QPushButton(self, text="sin")
		self.sin_button.move(cord_x, cord_y + 40)
		
		self.cos_button = QPushButton(self, text="cos")
		self.cos_button.move(cord_x + 100, cord_y + 40)
		
		self.tan_button = QPushButton(self, text="tan")
		self.tan_button.move(cord_x + 200, cord_y + 40)
		
		self.trig_output = QLabel(self)
		self.trig_output.move(cord_x + 135, cord_y + 20)
		self.trig_output.resize(1000, 30)
		self.tgb = QPushButton(self, text='Перейти в официальный тгк Калькулятора')
		self.tgb.move(750, 115)
		
		self.form_btn = QPushButton(self, text='Собщить об ошибке')
		self.form_btn.move(870, 150)
	
	def auto_scroll(self):
		cursor = self.history_text.textCursor()
		cursor.movePosition(QTextCursor.MoveOperation.End)
		self.history_text.setTextCursor(cursor)




if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	app.setWindowIcon(QIcon("calculator.ico"))
	window = Main()
	window.show()
	sys.exit(app.exec())