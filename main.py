from linear_regression_logic import perform_linear_regression
from plotting import plot_results

file_path = 'C:/Users/Анастасия/time_messagees.txt'  # Путь к файлу

# Линейная регрессия
X_test, y_test, y_pred, mse, r2 = perform_linear_regression(file_path)

# Вывод MSE и R2
print('Mean squared error: %.2f' % mse)
print('Coefficient of determination: %.2f' % r2)

# Отрисовка результатов
plot_results(X_test, y_test, y_pred)