from addings import *


def variance(numbers):
	"""Вычисляет дисперсию списка чисел."""
	mean = sum(numbers) / len(numbers)
	squared_diffs = [(num - mean) ** 2 for num in numbers]
	return sum(squared_diffs) / len(numbers)


def calculate_statistics(window, stat_type):
	"""Вычисляет статистику набора чисел (среднее, медиана, минимум, максимум, размах, дисперсия)."""
	try:
		numbers = list(map(float, window.entry_numbers.text().split()))
		print(numbers)
		if not numbers:
			return
		if stat_type == "mean":
			mean = sum(numbers) / len(numbers)
			final_result = dynamic_precision(mean)
			window.label_stat_result.setText(f"Среднее значение: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Среднее значение: {final_result}")
		elif stat_type == "median":
			sorted_numbers = sorted(numbers)
			mid = len(sorted_numbers) // 2
			median = (sorted_numbers[mid] + sorted_numbers[-mid - 1]) / 2 if len(sorted_numbers) % 2 == 0 else \
				sorted_numbers[mid]
			final_result = dynamic_precision(median)
			window.label_stat_result.setText(f"Медиана: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Медиана: {final_result}")
		elif stat_type == "max":
			maximum = max(numbers)
			final_result = dynamic_precision(maximum)
			
			window.label_stat_result.setText(f"Максимальное значение: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Максимальное значение: {final_result}")
		elif stat_type == "min":
			minimum = min(numbers)
			final_result = format_number(dynamic_precision(minimum))
			
			window.label_stat_result.setText(f"Минимальное значение: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Минимальное значение: {final_result}")
		elif stat_type == "range":
			rng = max(numbers) - min(numbers)
			final_result = dynamic_precision(rng)
			
			window.label_stat_result.setText(f"Размах: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Размах: {final_result}")
		elif stat_type == "variance":
			var = variance(numbers)
			final_result = dynamic_precision(var)
			
			window.label_stat_result.setText(f"Дисперсия: {final_result}")
			add_to_history(", ".join(map(str, numbers)), f"Дисперсия: {final_result}")
		else:
			raise ValueError(f"Неподдерживаемый тип статистики: {stat_type}")
		clear_errors(window)
		clear_labels(window, "label_stat_result")
		update_history(window)
		
	except ValueError as ve:
		handle_error(window, f"Ошибка: {ve}", input_data=window.entry_numbers.text(), function_name='calculate_statistics')
	except Exception as e:
		handle_error(window, f"Ошибка: {e}", input_data=window.entry_numbers.text(), function_name='calculate_statistics')


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
	
	
	app = QApplication(sys.argv)
	
	window = MyApp()
	window.entry_numbers.setText("5 34 12 34")
	window.show()
	calculate_statistics(window, 'mean')
	sys.exit(app.exec())

