from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QMessageBox, \
    QTabWidget, QVBoxLayout, QGridLayout, QHBoxLayout
import sys
from PyQt6.QtGui import QIcon, QTextCursor
from PyQt6.QtCore import QSize, Qt
from calculate import *
from equations import *
from statistic import *
from addings import *

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.box = QVBoxLayout(self)
        label_basic_calc_text = QLabel(self)
        label_basic_calc_text.setText("Введите числовое выражение (2+2):")
        label_basic_calc_text.move(0, 0)

        self.entry = QLineEdit()
        self.entry.move(0, 20)

        self.button_calc = QPushButton()

        self.button_calc.setText("Вычислить")
        self.button_calc.move(216, 15)


        self.label = QLabel()
        self.label.move(0, 40)
        self.label.resize(1000, 16)

        self.button_cor = QPushButton(text='√')
        self.button_cor.move(296, 15)
        self.box.addWidget(label_basic_calc_text)
        self.box.addWidget(self.entry)
        self.box.addWidget(self.label)
        self.box.addWidget(self.button_calc)
        
        self.box.addWidget(self.button_cor)
        self.box.addWidget(self.button_calc)
        print(self.button_calc)
        self.button_calc.clicked.connect(lambda: self.on_click())

        self.button_cor.clicked.connect(lambda: get_root_degree(self))
    def on_click(self):
        calculate(self)
    




class EqualationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QVBoxLayout(self)
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

        self.box.addWidget(label_system_of_equations_text)
        self.box.addWidget(self.entry_system_of_equations)
        self.box.addWidget(self.button_system_of_equations)
        self.box.addWidget(self.label_system_of_equations)
        self.button_system_of_equations.clicked.connect(lambda: self.on_click())
    def on_click(self):
        solve_system_of_equations(self)





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
        self.box = QVBoxLayout(self)
        
        self.box.addWidget(label_number_entry)
        self.box.addWidget(self.entry_numbers)
        self.box.addWidget(self.button_mean)
        self.box.addWidget(self.button_median)
        self.box.addWidget(self.button_max)
        self.box.addWidget(self.button_min)
        self.box.addWidget(self.button_range)
        self.box.addWidget(self.button_variance)
        self.box.addWidget(self.label_stat_result)
        self.button_mean.clicked.connect(lambda: self.on_click('mean'))
        self.button_median.clicked.connect(lambda: self.on_click('median'))
        self.button_max.clicked.connect(lambda: self.on_click('max'))
        self.button_min.clicked.connect(lambda: self.on_click('min'))
        self.button_range.clicked.connect(lambda: self.on_click('range'))
        self.button_variance.clicked.connect(lambda: self.on_click('variance'))
    def on_click(self, stat_type):
        try:
            
            numbers = list(map(float, self.entry_numbers.text().split()))
            print(numbers)
            if not numbers:
                return
            if stat_type == "mean":
                mean = sum(numbers) / len(numbers)
                final_result = dynamic_precision(mean)
                self.label_stat_result.setText(f"Среднее значение: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Среднее значение: {final_result}")
            elif stat_type == "median":
                sorted_numbers = sorted(numbers)
                mid = len(sorted_numbers) // 2
                median = (sorted_numbers[mid] + sorted_numbers[-mid - 1]) / 2 if len(sorted_numbers) % 2 == 0 else \
                    sorted_numbers[mid]
                final_result = dynamic_precision(median)
                self.label_stat_result.setText(f"Медиана: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Медиана: {final_result}")
            elif stat_type == "max":
                maximum = max(numbers)
                final_result = dynamic_precision(maximum)
                
                self.label_stat_result.setText(f"Максимальное значение: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Максимальное значение: {final_result}")
            elif stat_type == "min":
                minimum = min(numbers)
                final_result = format_number(dynamic_precision(minimum))
                
                self.label_stat_result.setText(f"Минимальное значение: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Минимальное значение: {final_result}")
            elif stat_type == "range":
                rng = max(numbers) - min(numbers)
                final_result = dynamic_precision(rng)
                
                self.label_stat_result.setText(f"Размах: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Размах: {final_result}")
            elif stat_type == "variance":
                var = variance(numbers)
                final_result = dynamic_precision(var)
                
                self.label_stat_result.setText(f"Дисперсия: {final_result}")
                add_to_history(", ".join(map(str, numbers)), f"Дисперсия: {final_result}")
            else:
                raise ValueError(f"Неподдерживаемый тип статистики: {stat_type}")
            
            
            
        
        except ValueError as ve:
            handle_error(ve, input_data=self.entry_numbers.text(), function_name="statistic")
        except Exception as e:
            handle_error(e, input_data=self.entry_numbers.text(), function_name="statistic")
        
from trinogremetric import *
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
        
        self.box = QVBoxLayout(self)
        self.box.addWidget(self.label_trig_text)
        self.box.addWidget(self.trig_input)
        self.box.addWidget(self.sin_button)
        self.box.addWidget(self.cos_button)
        self.box.addWidget(self.tan_button)
        self.box.addWidget(self.trig_output)
        self.sin_button.clicked.connect(lambda: self.on_click('sin'))
        self.cos_button.clicked.connect(lambda: self.on_click('cos'))
        self.tan_button.clicked.connect(lambda: self.on_click('tan'))
    def on_click(self, type):
        process_trigonometric_function(self, type)


class FractionUI(QWidget):
    def __init__(self):
        super().__init__()

        label_fractions_text = QLabel(self, text="Арифметика дробей:")
        label_fractions_text.move(0, 0)

        self.entry_first_fraction = QLineEdit(self)
        self.entry_first_fraction.move(0, 25)

        self.entry_second_fraction = QLineEdit(self)
        self.entry_second_fraction.move(165, 25)

        self.operator_variable = QComboBox(self)
        self.operator_variable.addItems(["+", "-", "*", "/"])
        self.operator_variable.move(135, 25)

        self.button_fractions_calculate = QPushButton(self, text="Выполнить операцию")
        self.button_fractions_calculate.move(0, 50)

        self.label_fractions_result = QLabel(self)
        self.label_fractions_result.move(0, 80)
        self.label_fractions_result.resize(300, 20)

        self.box = QGridLayout(self)

        self.box.addWidget(self.entry_first_fraction, 1, 0)

        self.box.addWidget(self.entry_second_fraction, 1, 2)
        self.box.addWidget(label_fractions_text, 0, 0)
        self.box.addWidget(self.button_fractions_calculate, 2, 0)
        self.box.addWidget(self.operator_variable, 1, 1)
        self.box.addWidget(self.label_fractions_result, 3, 0)
        self.button_fractions_calculate.clicked.connect(lambda: self.on_click())
    def on_click(self):
        arithmetic_operation_fractions(self, self.entry_first_fraction.text(), self.entry_second_fraction.text(), self.operator_variable.currentText())





class HistoryandError(QWidget):
    def __init__(self):
        
        super().__init__()

        self.error_text = QTextEdit(self)
        self.error_text.setReadOnly(True)
        self.error_text.resize(500, 150)
        
        self.history_text = QTextEdit(self)
        
        self.history_text.resize(600, 150)
        self.label_of_errors = QLabel(self, text='Поле с ошибками при вычислении:')
        
        self.cl_b = QPushButton(self, text="Очистить историю")
        
        self.box = QHBoxLayout(self)
        self.box.addWidget(self.label_of_errors)
        self.box.addWidget(self.error_text)
        self.box.addWidget(self.history_text)
        self.box.addWidget(self.cl_b)

        
    def auto_scroll(self):
        cursor = self.history_text.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.history_text.setTextCursor(cursor)
class NewApp(QWidget):
    def __init__(self):
        super().__init__()
        tab = QTabWidget(self)
        self.page = QWidget(tab)
        self.box = QHBoxLayout(self)
        calculator = Calculator()
        self.page.setLayout(calculator.box)
        tab.addTab(self.page, 'Калькулятор')
        page2 = QWidget(tab)
        equate = EqualationUI()
        page2.setLayout(equate.box)
        tab.addTab(page2, 'Решение уравнений')

        stati = StatisticUI()
        page3 = QWidget(tab)
        page3.setLayout(stati.box)
        tab.addTab(page3, 'Статистика')
        tab.setGeometry(0, 0, 800, 300)

        page4 = QWidget(tab)
        trigo = TrigonometryUI()
        page4.setLayout(trigo.box)
        tab.addTab(page4, "Тригонометрия")

        page5 = QWidget(tab)
        frac = FractionUI()
        page5.setLayout(frac.box)
        tab.addTab(page5, "Арифметика дробей")

        # self.history_text = QTextEdit(self)
        self.box.addWidget(tab)
        # self.box.addWidget(self.history_text)
        self.setGeometry(30, 30, 600, 300)
        
        


class Main(QWidget):
    def __init__(self):
        try:
            super().__init__()
        
            self.call_calculator = QPushButton("Калькулятор", self)
        
            self.call_equalation = QPushButton("Решатель уравнений", self)
        
            self.call_statistic = QPushButton("Подсчет статистики", self)
        
            self.call_trigonometry = QPushButton("Тригонометрия", self)
        
            self.call_fractions = QPushButton("Дробный решатель", self)
            self.tgb = QPushButton(self, text='Перейти в официальный тгк Калькулятора')
            self.tgb.move(0, 125)
            self.button_exit = QPushButton(self, text="Выход")
            self.button_exit.move(0, 175)
            self.form_btn = QPushButton(self, text='Сообщить об ошибке')
            self.form_btn.move(0, 150)
            self.call_history = QPushButton("История", self)
            self.call_calculator.move(0, 0)
            self.call_equalation.move(0, 20)
            self.call_statistic.move(0, 40)
            self.call_trigonometry.move(0, 60)
            self.call_fractions.move(0, 80)
            self.call_history.move(0, 100)
        except Exception as e:
            print(e)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Расширенный калькулятор")
        self.resize(1000, 1000)
        # Кнопка внутри окна
        self.msg_self.box = QMessageself.box(self)
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

        self.operator_variable = QComboself.box(self)
        self.operator_variable.addItems(["+", "-", "*", "/"])
        self.operator_variable.move(125, 310)

        self.button_fractions_calculate = QPushButton(self, text="Выполнить операцию")
        self.button_fractions_calculate.move(0, 338)

        self.label_fractions_result = QLabel(self)
        self.label_fractions_result.move(0, 363)
        self.label_fractions_result.resize(1000, 20)
        self.history_text = QTextEdit(self)
        self.history_text.move(0, 540)
        self.history_text.resize(600, 130)
        self.history_text.setReadOnly(True)
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

        self.form_btn = QPushButton(self, text='Сообщить об ошибке')
        self.form_btn.move(870, 150)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(sys.argv)
    app.setWindowIcon(QIcon("calculator.ico"))
    window = NewApp()
    window.show()
    sys.exit(app.exec())
