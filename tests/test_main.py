import main
from Classes import Product, Category


def test_main_func(capsys):
    """Тест запуска функции main() и проверки её вывода"""
    main.main()

    # Перехватываем весь вывод, который был сделан через print()
    captured = capsys.readouterr()


    assert "Samsung Galaxy S23 Ultra" in captured.out
    assert "256GB, Серый цвет, 200MP камера" in captured.out
    assert "180000.0" in captured.out
    assert "5" in captured.out

    assert "Iphone 15" in captured.out
    assert "210000.0" in captured.out
    assert "8" in captured.out

    assert "Xiaomi Redmi Note 11" in captured.out
    assert "31000.0" in captured.out
    assert "14" in captured.out

    assert "True" in captured.out
    assert "27" in captured.out
    assert "3" in captured.out

    assert "Телевизоры" in captured.out
