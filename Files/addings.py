import logging
from decimal import Decimal, getcontext
import traceback
from PyQt6.QtWidgets import QMessageBox
from sympy import Float
history = []


def dynamic_precision(value):
    getcontext().prec = 30

    if isinstance(value, (int, float)):
        decimal_value = Decimal(str(value))
        order = int(decimal_value.adjusted())
        rounded_value = decimal_value.normalize()
        precision = max(6, -order + 6)
        logging.info(format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.'))
        return format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.')

    elif isinstance(value, complex):
        real_part = dynamic_precision(value.real)
        imag_part = dynamic_precision(value.imag)
        return complex(real_part, imag_part)

    elif isinstance(value, str):
        logging.info(f'Это строка {value}')
        return value

    elif isinstance(value, list) or isinstance(value, tuple):
        return type(value)(map(dynamic_precision, value))
    elif isinstance(value, Float):
        value = float(value)
        decimal_value = Decimal(str(value))
        order = int(decimal_value.adjusted())
        rounded_value = decimal_value.normalize()
        precision = max(2, -order + 2)
        logging.info(format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.'))
        return format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.')
    else:
        type_of = type(value)
        logging.info(f'Не определён тип {type_of}')
        return value


def clear_labels(window, lb):
    labels = ["label_stat_result", "trig_output", "label_fractions_result", "label_system_of_equations", "label"]
    for cll in labels:
        if cll != lb:
            window.cll.clear()


def handle_error(window, error_message, input_data=None, function_name=None, lb=None):
    """
    Функция для обработки ошибок с дополнительными параметрами.
    :param error_message: Сообщение об ошибке.
    :param input_data: Данные, введенные пользователем.
    :param function_name: Имя функции, в которой произошла ошибка.
    """
    # Вызывает ошибку

    window.error_text.clear()

    # Добавляем дополнительную информацию в сообщение об ошибке
    full_error_message = f"{error_message}"
    if function_name:
        full_error_message += f"\nФункция: {function_name}"
    if input_data:
        full_error_message += f"\nВвод: {input_data}"

    # Включаем трассировку стека для получения полной картины ошибки
    stack_trace = traceback.format_exc()
    full_error_message += f"\nТрассировка стека:\n{stack_trace}"

    # Специальное сообщение для конкретной ошибки
    if "not enough values to unpack (expected 2, got 1)" in error_message:
        full_error_message = "Ошибка: Вы не ввели знак '='. Пожалуйста, введите '=' и получите ответ."
    elif 'деление на ноль' in error_message:
        full_error_message = 'Ошибка: Вы реально поделили на ноль? Вы не знаете правило математики?!'
    elif "Sympify of expression 'could not parse" in error_message:
        full_error_message = 'Не выполняйте код'
    window.error_text.setText(full_error_message)


    # Добавляем ошибку в историю


def add_to_history(expression, result):
    if str(result).startswith("Ошибка:"):
        # Очищаем запись об ошибке
        history.append((expression, str(result).split(":")[0]))
    else:
        # Формируем правильную запись с результатом
        history.append((expression, str(result)))


def update_history(window):
      # Временное разрешение редактирования
    window.history_text.clear()  # Очищаем текущее содержимое
    for i, (expr, res) in enumerate(history):
        if str(res).startswith("Ошибка:"):
            window.history_text.insertPlainText(f"{i + 1}. {expr} = {res}\n")
        else:
            window.history_text.insertPlainText(f"{i + 1}. {expr} = {res}\n")



def clear_errors(window):
    """Очищает поле ошибок."""

    window.error_text.clear()


def clear_history(window):
    """Очищает историю вычислений."""
    history.clear()
    update_history(window)


if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox
    import sys
    from PyQt6.QtGui import QIcon
    from PyQt6.QtCore import QSize


    class MyApp(QWidget):
        def __init__(self):
            super().__init__()

            # Настройка окна
            self.setWindowTitle("Расширенный калькулятор")
            self.resize(1000, 1000)
            label_basic_calc_text = QLabel(self)
            label_basic_calc_text.setText("Введите числовое выражение (2+2):")
            label_basic_calc_text.move(0, 0)

            self.msg_box = QMessageBox(self)

            self.entry = QLineEdit(self)
            self.entry.move(0, 20)

            self.button_calc = QPushButton(self)

            self.button_calc.setText("Вычислить")
            self.button_calc.move(216, 15)

            self.label = QLabel(self)
            self.label.move(0, 40)
            self.label.resize(1000, 16)


    app = QApplication(sys.argv)

    window = MyApp()
    window.show()
    handle_error(window, "Ошибка", input_data="2+2", function_name="Hello")
    sys.exit(app.exec())
