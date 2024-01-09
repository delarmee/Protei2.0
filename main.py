from linear_regression_logic import perform_linear_regression
from plotting import plot_results

file_path = 'C:/Users/Анастасия/time_messagees.txt'  # Путь к файлу

X_test, y_test, y_pred, mse, r2 = perform_linear_regression(file_path)

print('Mean squared error: %.2f' % mse)
print('Coefficient of determination: %.2f' % r2)

plot_results(X_test, y_test, y_pred)