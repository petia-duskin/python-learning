# dictionary comprehension

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)

# filter dictionary

new_stocks2 = {symbol: price for (symbol, price) in stocks.items() if price > 200}

print(new_stocks2)
