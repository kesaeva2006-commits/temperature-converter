def celsius_to_fahrenheit(c):
    """Перевод из Цельсия в Фаренгейт"""
    return round(c * 9/5 + 32, 2)

def fahrenheit_to_celsius(f):
    """Перевод из Фаренгейта в Цельсий"""
    return round((f - 32) * 5/9, 2)

def celsius_to_kelvin(c):
    """Перевод из Цельсия в Кельвин"""
    return round(c + 273.15, 2)

def kelvin_to_celsius(k):
    """Перевод из Кельвина в Цельсий"""
    return round(k - 273.15, 2)
