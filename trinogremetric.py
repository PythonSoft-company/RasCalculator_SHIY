import addings
import math
from sympy import *

def process_trigonometric_function(window, function_type):
	"""Вычисляет тригонометрическую функцию указанного типа."""
	try:
		angle = float(window.trig_input.text())
		radians = math.radians(angle)
		if function_type == 'sin':
			result = math.sin(radians)
		elif function_type == 'cos':
			result = math.cos(radians)
		elif function_type == 'tan':
			result = math.tan(radians)
		elif function_type == 'arcsin':
			result = math.degrees(math.asin(math.degrees(radians)))
		elif function_type == 'arccos':
			result = math.degrees(math.acos(math.degrees(radians)))
		elif function_type == 'arctan':
			result = math.degrees(math.atan(math.degrees(radians)))
		
		else:
			raise ValueError(f'Неверный тип тригонометрической функции: {function_type}')
		final_result = addings.format_number(addings.dynamic_precision(result))
		window.trig_output.setText(f"{final_result}")
		
	except ValueError as ve:
		print(ve)
		addings.handle_error(str(ve), input_data=window.trig_input.text(), function_name="process_trigonometric_function")
	except Exception as e:
		print(e)
		addings.handle_error(str(e), input_data=window.trig_input.text(), function_name="process_trigonometric_function")