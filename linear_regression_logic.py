import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def perform_linear_regression(file_path):
    """
    Функция выполняет линейную регрессию на данных из файла и возвращает результаты.

    Parameters:
        file_path (str): Путь к файлу с данными.

    Returns:
        X_test (numpy array): Тестовые значения переменной X.
        y_test (numpy array): Тестовые значения зависимой переменной y.
        y_pred (numpy array): Предсказанные значения зависимой переменной y.
        mse (float): Среднеквадратичная ошибка.
        r2 (float): Коэффициент детерминации.
    """
    data = pd.read_csv(file_path, delimiter=',', names=['время', 'количество_сообщений'])
    data['время'] = pd.to_datetime(data['время'], format='%H:%M:%S').dt.hour
    X = data['время'].values.reshape(-1, 1)
    y = data['количество_сообщений'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return X_test, y_test, y_pred, mse, r2

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return X_test, y_test, y_pred, mse, r2