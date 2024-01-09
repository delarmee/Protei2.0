import pandas as pd

def load_and_filter_data(file_path, lower_quantile=0.05, upper_quantile=0.95):
    data = pd.read_csv(file_path, delimiter=',', names=['время', 'количество_сообщений'])

    # Определение квантилей для выбросов
    lower_bound = data['количество_сообщений'].quantile(lower_quantile)
    upper_bound = data['количество_сообщений'].quantile(upper_quantile)

    # Фильтрация выбросов
    filtered_data = data[(data['количество_сообщений'] >= lower_bound) & (data['количество_сообщений'] <= upper_bound)]

    return filtered_data