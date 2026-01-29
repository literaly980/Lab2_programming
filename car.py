"""
Лабораторная работа №2: Объектно-ориентированное программирование
Классы автомобилей с наследованием и перегрузкой методов
"""

from abc import ABC, abstractmethod
from typing import Union


class Car(ABC):
    """
    Базовый класс автомобиля
    """
    
    def __init__(self, brand: str, model: str, year: int, color: str, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self._engine_running = False
        self._current_speed = 0
    
    # Свойства
    @property
    def brand(self) -> str:
        """Марка автомобиля"""
        return self._brand
    
    @brand.setter
    def brand(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Марка должна быть непустой строкой")
        self._brand = value.capitalize()
    
    @property
    def model(self) -> str:
        """Модель автомобиля"""
        return self._model
    
    @model.setter
    def model(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Модель должна быть непустой строкой")
        self._model = value
    
    @property
    def year(self) -> int:
        """Год выпуска"""
        return self._year
    
    @year.setter
    def year(self, value: int):
        current_year = 2025
        if not isinstance(value, int) or value < 1900 or value > current_year + 1:
            raise ValueError(f"Год должен быть числом от 1900 до {current_year + 1}")
        self._year = value
    
    @property
    def color(self) -> str:
        """Цвет автомобиля"""
        return self._color
    
    @color.setter
    def color(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Цвет должен быть непустой строкой")
        self._color = value.lower()
    
    @property
    def price(self) -> float:
        """Цена автомобиля"""
        return self._price
    
    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self._price = float(value)
    
    # Методы
    def start_engine(self) -> str:
        """Запустить двигатель"""
        if not self._engine_running:
            self._engine_running = True
            return f"Двигатель {self.brand} {self.model} запущен"
        return f"Двигатель {self.brand} {self.model} уже работает"
    
    def stop_engine(self) -> str:
        """Остановить двигатель"""
        if self._engine_running:
            self._engine_running = False
            self._current_speed = 0
            return f"Двигатель {self.brand} {self.model} остановлен"
        return f"Двигатель {self.brand} {self.model} уже выключен"
    
    def accelerate(self, speed: int) -> str:
        """Увеличить скорость"""
        if not self._engine_running:
            return f"Сначала запустите двигатель {self.brand} {self.model}"
        
        if speed < 0:
            return "Скорость не может быть отрицательной"
        
        self._current_speed = min(self._current_speed + speed, self.get_max_speed())
        return f"Скорость увеличена до {self._current_speed} км/ч"
    
    def brake(self, intensity: int) -> str:
        """Торможение"""
        if not self._engine_running:
            return f"Двигатель {self.brand} {self.model} не работает"
        
        if intensity < 0:
            return "Интенсивность торможения не может быть отрицательной"
        
        self._current_speed = max(self._current_speed - intensity, 0)
        return f"Скорость снижена до {self._current_speed} км/ч"
    
    def get_info(self) -> str:
        """Получить информацию об автомобиле"""
        return f"{self.brand} {self.model} ({self.year}) - {self.color}, ${self.price:.2f}"
    
    # Перегружаемые методы
    def get_max_speed(self) -> int:
        """Получить максимальную скорость"""
        return 200  # Базовое значение
    
    def get_fuel_type(self) -> str:
        """Получить тип топлива"""
        return "бензин"  # Базовое значение
    
    @abstractmethod
    def get_special_features(self) -> list:
        """Получить особые характеристики"""
        pass


class BMW(Car):
    """
    Класс BMW - наследник базового класса Car
    """
    
    def __init__(self, model: str, year: int, color: str, price: float, 
                 series: str, drive_type: str = "задний"):
        super().__init__("BMW", model, year, color, price)
        self.series = series  # Серия (3, 5, 7, X, etc.)
        self.drive_type = drive_type  # Тип привода
        self._sport_mode = False
    
    # Дополнительные свойства
    @property
    def series(self) -> str:
        """Серия BMW"""
        return self._series
    
    @series.setter
    def series(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Серия должна быть непустой строкой")
        self._series = value
    
    @property
    def drive_type(self) -> str:
        """Тип привода"""
        return self._drive_type
    
    @drive_type.setter
    def drive_type(self, value: str):
        valid_types = ["задний", "передний", "полный"]
        if value.lower() not in valid_types:
            raise ValueError(f"Тип привода должен быть одним из: {valid_types}")
        self._drive_type = value.lower()
    
    # Перегрузка методов
    def get_max_speed(self) -> int:
        """Перегрузка метода максимальной скорости"""
        base_speed = super().get_max_speed()
        if self.series in ["M", "M3", "M5", "M8"]:
            return base_speed + 80  # M-серии быстрее
        elif self.series in ["7", "8"]:
            return base_speed + 40  # Премиум серии
        elif self.series in ["X5", "X6", "X7"]:
            return base_speed + 20  # SUV серии
        return base_speed + 30  # Остальные BMW
    
    def get_fuel_type(self) -> str:
        """Перегрузка метода типа топлива"""
        if self.series in ["i3", "i4", "iX", "i7"]:
            return "электричество"
        elif self.series in ["330e", "530e", "745e"]:
            return "гибрид"
        return "бензин"
    
    # Дополнительные методы
    def activate_sport_mode(self) -> str:
        """Активировать спортивный режим"""
        if not self._engine_running:
            return f"Запустите двигатель {self.brand} {self.model} для активации спортивного режима"
        
        self._sport_mode = True
        return f"Спортивный режим {self.brand} {self.model} активирован"
    
    def deactivate_sport_mode(self) -> str:
        """Деактивировать спортивный режим"""
        self._sport_mode = False
        return f"Спортивный режим {self.brand} {self.model} деактивирован"
    
    def get_special_features(self) -> list:
        """Особые характеристики BMW"""
        features = [f"Серия: {self.series}", f"Привод: {self.drive_type}"]
        if self._sport_mode:
            features.append("Спортивный режим: активен")
        if self.series.startswith("i"):
            features.append("Электромобиль")
        elif "e" in self.series:
            features.append("Гибрид")
        return features


class Mercedes(Car):
    """
    Класс Mercedes - наследник базового класса Car
    """
    
    def __init__(self, model: str, year: int, color: str, price: float,
                 class_type: str, amg_package: bool = False):
        super().__init__("Mercedes-Benz", model, year, color, price)
        self.class_type = class_type  # Класс (A, C, E, S, G, etc.)
        self.amg_package = amg_package  # AMG пакет
        self._comfort_mode = True
    
    # Дополнительные свойства
    @property
    def class_type(self) -> str:
        """Класс Mercedes"""
        return self._class_type
    
    @class_type.setter
    def class_type(self, value: str):
        valid_classes = ["A", "B", "C", "E", "S", "G", "GLA", "GLC", "GLE", "GLS"]
        if not value or value.upper() not in valid_classes:
            raise ValueError(f"Класс должен быть одним из: {valid_classes}")
        self._class_type = value.upper()
    
    @property
    def amg_package(self) -> bool:
        """Наличие AMG пакета"""
        return self._amg_package
    
    @amg_package.setter
    def amg_package(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("AMG пакет должен быть булевым значением")
        self._amg_package = value
    
    # Перегрузка методов
    def get_max_speed(self) -> int:
        """Перегрузка метода максимальной скорости"""
        base_speed = super().get_max_speed()
        if self.amg_package:
            return base_speed + 100  # AMG версии значительно быстрее
        elif self.class_type in ["S", "SL", "GT"]:
            return base_speed + 60  # Премиум класс
        elif self.class_type.startswith("G"):
            return base_speed + 10  # G-класс (внедорожник)
        return base_speed + 25  # Остальные Mercedes
    
    def get_fuel_type(self) -> str:
        """Перегрузка метода типа топлива"""
        if self.model.startswith("EQ"):
            return "электричество"
        elif "e" in self.model.lower():
            return "гибрид"
        elif self.amg_package:
            return "бензин (высокооктановый)"
        return "бензин"
    
    # Дополнительные методы
    def activate_comfort_mode(self) -> str:
        """Активировать комфортный режим"""
        self._comfort_mode = True
        return f"Комфортный режим {self.brand} {self.model} активирован"
    
    def deactivate_comfort_mode(self) -> str:
        """Деактивировать комфортный режим"""
        self._comfort_mode = False
        return f"Комфортный режим {self.brand} {self.model} деактивирован"
    
    def get_special_features(self) -> list:
        """Особые характеристики Mercedes"""
        features = [f"Класс: {self.class_type}"]
        if self.amg_package:
            features.append("AMG пакет: установлен")
        if self._comfort_mode:
            features.append("Комфортный режим: активен")
        if self.model.startswith("EQ"):
            features.append("Электромобиль")
        elif "e" in self.model.lower():
            features.append("Гибрид")
        return features


def main():
    """
    Демонстрация работы классов
    """
    print("=== Лабораторная работа №2: Объектно-ориентированное программирование ===\n")
    
    # Создание объектов
    print("Создание автомобилей:")
    bmw_m3 = BMW("M3", 2024, "синий", 85000, "M3", "задний")
    mercedes_s500 = Mercedes("S500", 2024, "черный", 120000, "S", False)
    bmw_ix = BMW("iX", 2024, "белый", 95000, "iX", "полный")
    mercedes_amg = Mercedes("C63 AMG", 2024, "серый", 95000, "C", True)
    
    # Демонстрация работы
    cars = [bmw_m3, mercedes_s500, bmw_ix, mercedes_amg]
    
    for i, car in enumerate(cars, 1):
        print(f"\n--- Автомобиль {i} ---")
        print(car.get_info())
        print(f"Максимальная скорость: {car.get_max_speed()} км/ч")
        print(f"Тип топлива: {car.get_fuel_type()}")
        print(f"Особые характеристики: {', '.join(car.get_special_features())}")
        
        # Демонстрация методов
        print(car.start_engine())
        print(car.accelerate(100))
        print(car.brake(30))
        print(car.stop_engine())
    
    print("\n=== Демонстрация специальных возможностей ===")
    
    # BMW спортивный режим
    print("\nBMW M3 - спортивный режим:")
    bmw_m3.start_engine()
    print(bmw_m3.activate_sport_mode())
    print(bmw_m3.accelerate(150))
    print(bmw_m3.deactivate_sport_mode())
    bmw_m3.stop_engine()
    
    # Mercedes комфортный режим
    print("\nMercedes S500 - комфортный режим:")
    mercedes_s500.start_engine()
    print(mercedes_s500.activate_comfort_mode())
    print(mercedes_s500.accelerate(80))
    print(mercedes_s500.deactivate_comfort_mode())
    mercedes_s500.stop_engine()
    
    print("\n=== Программа завершена ===")


if __name__ == "__main__":
    main()
