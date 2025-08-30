
# Модуль для анализа сигналов и квадратов
def analyze_signals(data):
    signals = []

    for coin, price in data.items():
        if coin == "BTCUSDT" and float(price) > 25000:
            signals.append({
                "coin": coin,
                "timeframe": "1h",
                "signal": "Price above 25000, possible breakout",
                "price": price
            })

    return signals
