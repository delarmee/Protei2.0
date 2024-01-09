from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression


def perform_polynomial_regression(X, y, degree):
    # Создание модели полиномиальной регрессии
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    # Обучение модели
    model.fit(X, y)

    return model