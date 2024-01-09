import matplotlib.pyplot as plt

def plot_results(X_test, y_test, y_pred):
    """
    Функция отрисовывает график реальных и предсказанных значений.

    Parameters:
        X_test (numpy array): Тестовые значения переменной X.
        y_test (numpy array): Тестовые значения зависимой переменной y.
        y_pred (numpy array): Предсказанные значения зависимой переменной y.
    """
    plt.scatter(X_test, y_test, color='grey', label='real scikit-learn')
    plt.plot(X_test, y_pred, color='blue', linewidth=1, label='prediction scikit-learn')
    plt.title('График данных')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()