from sympy import *
from addings import *
from fractions import Fraction
import math
from decimal import Decimal, getcontext
def replace_caret_with_power(expression):
	"""Заменяет символ ^ на оператор возведения в степень (**)."""
	return expression.replace('^', '**')


def replace_z_t(expression):
	"""Заменяет запятую на точку в числе."""
	return expression.replace(',', '.')








def nth_root(number, n):
	"""Вычисляет корень n-й степени из числа."""
	if number < 0 and n % 2 == 0:
		raise ValueError("Корень четной степени из отрицательного числа невозможен.")
	return number ** (1 / n)


def calculate(windows):
	try:
		expression = windows.entry.text()
		expression = replace_z_t(expression)
		expression = replace_caret_with_power(expression)
		print(expression)
		if expression == "":
			return
		if '0' in expression and '/' in expression:
			parts = expression.split('/')
			if parts[1].strip() == '0':
				raise ZeroDivisionError
		if '!' in expression:
			expression = expression.replace('!', '')
			result = factorial_scientific(int(expression))
			final_result = dynamic_precision(result)
			mantissa, exponent = final_result.split("E")
			final_result = "{}*10^{}".format(float(mantissa), int(exponent))
			add_to_history(expression, final_result)
			update_history(windows)
			windows.label.setText(f"{final_result}")
			clear_errors(windows)
			clear_labels(windows, 'label')
			
			return
		elif '√' in expression:
			parts = expression.split('√')
			if len(parts) != 2:
				raise ValueError("Неверный формат корня")
			n = int(parts[0])
			x = int(parts[1])
			result = nth_root(x, n)
		else:
			result = sympify(expression).evalf()
			logging.info(result)
			result = float(result)
		
		# Применение динамической точности
		final_result = format_number(dynamic_precision(result))
		add_to_history(expression, final_result)
		update_history(windows)
		windows.label.setText(f"{final_result}")
		clear_errors(windows)
		
		clear_labels(windows, "label")
	
	except ZeroDivisionError:
		handle_error(window=windows, error_message="Ошибка: деление на ноль.", input_data=expression, function_name='calculate', lb="label")
	except ValueError as ve:
		handle_error(window=windows, error_message=f"Ошибка: {ve}", input_data=expression, function_name='calculate')
	except SyntaxError:
		handle_error(window=windows, error_message="Ошибка: синтаксическая ошибка в выражении.", function_name='calculate',
		             )
	except Exception as e:
		handle_error(window=windows,error_message=f"Ошибка: {e}", function_name='calculate')













def factorial_scientific(n):
	"""
	Представляет факториал числа в научной форме.

	Параметры:
	- n: Число, факториал которого нужно представить.

	Возвращает:
	Строку с представлением факториала в научной форме.
	"""
	if not isinstance(n, int) or n < 0:
		raise ValueError("Факториал определен только для неотрицательных целых чисел")
	
	# Устанавливаем высокую точность для работы с большими числами
	getcontext().prec = 100  # Можно увеличить точность при необходимости
	
	# Рассчитываем факториал
	fact = Decimal(1)
	for i in range(1, n + 1):
		fact *= Decimal(i)
	
	# Представляем в научной форме
	scientific_representation = "{:.5E}".format(fact.normalize())
	
	return scientific_representation




def arithmetic_operation_fractions(window, first_fraction, second_fraction, operation):
	"""Производит арифметические операции с дробями."""
	try:
		frac1 = Fraction(first_fraction)
		frac2 = Fraction(second_fraction)
		if operation == "+":
			result = frac1 + frac2
		elif operation == "-":
			result = frac1 - frac2
		elif operation == "*":
			result = frac1 * frac2
		elif operation == "/":
			result = frac1 / frac2
		else:
			raise ValueError("Операция не поддерживается.")
		window.label_fractions_result.setText(f"Результат: {result}")
		clear_errors(window)
		add_to_history(f"{frac1} {operation} {frac2}", result)
		update_history(window)
		clear_labels(window, 'label_fractions_result')
	except ZeroDivisionError:
		handle_error(window, "Ошибка: деление на ноль.", input_data=(first_fraction, second_fraction),
		             function_name='arithmetic_operation_fractions')
	except ValueError as ve:
		handle_error(window, f"Ошибка: {ve}", input_data=(first_fraction, second_fraction),
		             function_name='arithmetic_operation_fractions')
	except Exception as e:
		handle_error(window, f"Ошибка: {e}", input_data=(first_fraction, second_fraction),
		             function_name='arithmetic_operation_fractions')