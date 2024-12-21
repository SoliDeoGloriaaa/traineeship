import yfinance as yf
from pathlib import Path

def fetch_stock_data(ticker, period='1mo'):
    """
    Метод для получения исторических данных о ценах акций для заданного тикера.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Метод добавляет скользящее среднее к данным о ценах акций.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Метод вычисляет и выводит среднюю цену закрытия акций за заданный период.
    """
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия акций: {average_price:.2f}")
    else:
        print("Данные не содержат колонку 'Close'.")


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные и уведомляет пользователя.
    Если цена акций колебалась более чем на заданный процент за период.
    """
    if 'Close' in data.columns:
        max_price = data['Close'].max()
        min_price = data['Close'].min()
        difference = ((max_price - min_price) / min_price) * 100

        if difference > threshold:
            print(f"Уведомление: Цена акций колебалась более чем на {threshold}% за период. "
                  f"Колебание: {difference:.2f}%")
    else:
        print("Данные не содержат колонку 'Close'.")


def export_data_to_csv(data, filename):
    """
    Экспрот данных в CSV формат.
    """
    directory = Path("D:/DEV/project_1/csv")
    filepath = directory / filename
    directory.mkdir(parents=True, exist_ok=True)
    
    try:
        data.to_csv(filepath, index=False)
        print(f"Данные успешно сохранены в {filepath}.")
    except Exception as error:
        print(f"Произошла ошибка при сохранении данных: {error}")

