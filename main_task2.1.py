from data_processing_module import load_and_filter_data
from regression_module import perform_polynomial_regression
from plotting_module import plot_results

file_path = 'C:/Users/Анастасия/time_messagees.txt'

# Загрузка и фильтрация данных
filtered_data = load_and_filter_data(file_path)

# Подготовка данных для регрессии
X = filtered_data['время'].values.reshape(-1, 1)
y = filtered_data['количество_сообщений'].values

# Выбор степени полинома
degree = 3

# Полиномиальная регрессия
model = perform_polynomial_regression(X, y, degree)

# Отрисовка результатов
plot_results(X, y, model, degree)