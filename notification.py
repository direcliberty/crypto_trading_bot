
import telegram

# Функция для отправки уведомлений через Telegram
def send_telegram_notification(signal):
    bot = telegram.Bot(token='your_telegram_token')
    message = f"🚨 New Signal for {signal['coin']}
"               f"Timeframe: {signal['timeframe']}
"               f"Signal: {signal['signal']}
"               f"Price: {signal['price']} USDT"
    bot.send_message(chat_id='your_chat_id', text=message)
