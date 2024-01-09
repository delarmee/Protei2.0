import matplotlib.pyplot as plt

def plot_results(X, y, model, degree):
    # Предсказание значений
    y_pred = model.predict(X)

    # Отрисовка результатов
    plt.scatter(X, y, color='grey', label='Real data')
    plt.plot(X, y_pred, label=f'Degree {degree}', linewidth=2)

    plt.title('Полиномиальная регрессия')
    plt.xlabel('Время')
    plt.ylabel('Количество сообщений')
    plt.legend()
    plt.show()