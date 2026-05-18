from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

def test_celsius_to_fahrenheit():
    """Тест перевода из Цельсия в Фаренгейт"""
    # 0°C = 32°F, 100°C = 212°F
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0

def test_fahrenheit_to_celsius():
    """Тест перевода из Фаренгейта в Цельсий"""
    # 32°F = 0°C, 212°F = 100°C
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0

def test_celsius_to_kelvin():
    """Тест перевода из Цельсия в Кельвин"""
    # 0°C = 273.15K, 100°C = 373.15K
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15

def test_kelvin_to_celsius():
    """Тест перевода из Кельвина в Цельсий"""
    # 273.15K = 0°C, 373.15K = 100°C
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(373.15) == 100.0
