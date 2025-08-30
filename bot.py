
import logging
import telegram
from data_fetch import fetch_data
from signal_analysis import analyze_signals
from notification import send_telegram_notification

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Токен для Telegram-бота
TELEGRAM_TOKEN = 'your_telegram_token'
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Функция для обработки сигналов
def main():
    # Получение данных
    data = fetch_data()

    # Пример вызова анализа сигналов
    signals = analyze_signals(data)

    for signal in signals:
        # Отправка уведомления в Telegram
        send_telegram_notification(signal)
        logging.info(f"Signal sent for {signal['coin']}")

# Запуск бота
if __name__ == '__main__':
    main()
