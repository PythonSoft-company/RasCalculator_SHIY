try:
	import addings
except Exception as e:
	print(e)


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
			final_result = addings.dynamic_precision(mean)
			window.label_stat_result.setText(f"Среднее значение: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Среднее значение: {final_result}")
		elif stat_type == "median":
			sorted_numbers = sorted(numbers)
			mid = len(sorted_numbers) // 2
			median = (sorted_numbers[mid] + sorted_numbers[-mid - 1]) / 2 if len(sorted_numbers) % 2 == 0 else \
				sorted_numbers[mid]
			final_result = addings.dynamic_precision(median)
			window.label_stat_result.setText(f"Медиана: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Медиана: {final_result}")
		elif stat_type == "max":
			maximum = max(numbers)
			final_result = addings.dynamic_precision(maximum)
			
			window.label_stat_result.setText(f"Максимальное значение: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Максимальное значение: {final_result}")
		elif stat_type == "min":
			minimum = min(numbers)
			final_result = addings.dynamic_precision(minimum)
			
			window.label_stat_result.setText(f"Минимальное значение: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Минимальное значение: {final_result}")
		elif stat_type == "range":
			rng = max(numbers) - min(numbers)
			final_result = addings.dynamic_precision(rng)
			
			window.label_stat_result.setText(f"Размах: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Размах: {final_result}")
		elif stat_type == "variance":
			var = variance(numbers)
			final_result = addings.dynamic_precision(var)
			
			window.label_stat_result.setText(f"Дисперсия: {final_result}")
			addings.add_to_history(", ".join(map(str, numbers)), f"Дисперсия: {final_result}")
		else:
			raise ValueError(f"Неподдерживаемый тип статистики: {stat_type}")
		
		
		
		
	except ValueError as ve:
		print(ve)
		handle_error(ve, input_data=window.entry_numbers.text(), function_name="calculate_statistics")
	except Exception as e:
		print(e)
		handle_error(e, input_data=window.entry_numbers.text(), function_name="calculate_statistics")



