from typing import Union
import doctest


class Song:
    def __init__(self, title: str, artist: str, length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Песня"

        :param title: Название песни
        :param artist: Имя исполнителя
        :param length: Длительность песни (в минутах)

        Примеры:
        >>> my_song = Song("Люди", "Дайте танк (!)", 2.56)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError
        self.title = title
        if not isinstance(artist, str):
            raise TypeError
        self.artist = artist
        if not isinstance(length, (int, float)):
            raise TypeError
        if length < 0:
            raise ValueError
        self.length = length

    def increase_length(self, additional_length: Union[int, float]) -> None:
        """
        Функция увеличивает длительность песни
        :param additional_length: Добавляемая длительность (в минутах)

        :raise ValueError: Если количество добавлеяемой длительности <0, то кидаем исключение

        Примеры:
        >>> my_song = Song("Люди", "Дайте танк (!)", 2.56)
        >>> my_song.increase_length(1.2)
        """
        if not isinstance(additional_length, (int, float)):
            raise TypeError("Добавляемая длительность должна быть типа int или float")
        if additional_length < 0:
            raise ValueError("Добавляемая длительность должна неотрицательным числом")
        ...

    def decrease_length(self, length_to_remove: Union[int, float]) -> None:
        """
        Функция уменьшает длительность песни
        :param length_to_remove: Удаляемая длительность (в минутах)

        :raise ValueError: Если количество удаляемой длительности <0, то кидаем исключение
        :raise ValueError: Если количество удаляемой длительности больше исходной, то кидаем исключение

        Примеры:
        >>> my_song = Song("Люди", "Дайте танк (!)", 2.56)
        >>> my_song.decrease_length(1.81)
        """
        if not isinstance(length_to_remove, (int, float)):
            raise TypeError("Удаляемая длительность должна быть типа int или float")
        if length_to_remove < 0:
            raise ValueError("Удаляемая длительность должна неотрицательным числом")
        if self.length < length_to_remove:
            raise ValueError("Удаляемая длительность не должна превышать исходную")
        ...


class Photo:
    def __init__(self, is_black_and_white: bool, width: Union[int, float], length: Union[int, float]):
        """
           Создание и подготовка к работе объекта "Фото"

           :param is_black_and_white: Состояние фото по цвету (ЧБ - True, ЦВЕТ - False)
           :param width: Ширина фото (см)
           :param length: Длина фото (см)

           Примеры:
           >>> photo_by_me = Photo(True, 7, 9.5)  # инициализация экземпляра класса
           """
        if not isinstance(is_black_and_white, bool):
            raise TypeError
        self.is_black_and_white = is_black_and_white
        if not isinstance(width, (int, float)):
            raise TypeError
        if width < 0:
            raise ValueError
        self.width = width
        if not isinstance(length, (int, float)):
            raise TypeError
        if length < 0:
            raise ValueError
        self.length = length

    def crop_photo(self, width_to_remove: Union[int, float], length_to_remove: Union[int, float]) -> None:
        """
        Функция обрезает фото
        :param width_to_remove: Удаляемая ширина (см)
        :param length_to_remove: Удаляемая длина (см)

        :raise ValueError: Если удаляемая длина или ширина <0, то кидаем исключение
        :raise ValueError: Если удаляемая длина или ширина превышает исходную, то кидаем исключение

        Примеры:
        >>> photo_by_me = Photo(True, 7, 9.5)
        >>> photo_by_me.crop_photo(2, 1.5)
        """
        if not isinstance(width_to_remove, (int, float)):
            raise TypeError("Удаляемая ширина должна быть типа int или float")
        if not isinstance(length_to_remove, (int, float)):
            raise TypeError("Удаляемая длина должна быть типа int или float")
        if length_to_remove < 0 or width_to_remove < 0:
            raise ValueError("Удаляемые длина и ширина должны быть неотрицательными числами")
        if self.length < length_to_remove or self.width < width_to_remove:
            raise ValueError("Удаляемые длина и ширина не должны превышать исходные")
        ...

    def turn_photo(self) -> None:
        """
        Функция переворачивает фото (меняет длину и ширину местами)

        Примеры:
        >>> photo_by_me = Photo(True, 7, 9.5)
        >>> photo_by_me.turn_photo()
        """
        ...

    def make_colorful(self) -> None:
        """
        Функция меняет состояние фото, делая его цветным

        Примеры:
        >>> photo_by_me = Photo(True, 7, 9.5)
        >>> photo_by_me.make_colorful()
        """
        ...


class Car:
    def __init__(self, brand: str, current_speed: int, count_of_seats: int):
        """
           Создание и подготовка к работе объекта "Машина"

           :param brand: Марка машины
           :param current_speed: Текущая скорость (км/ч)
           :param count_of_seats: Количество посадочных мест

           Примеры:
           >>> my_car = Car("Audi", 120, 5)  # инициализация экземпляра класса
           """
        if not isinstance(brand, str):
            raise TypeError
        self.brand = brand
        if not isinstance(current_speed, int):
            raise TypeError
        if current_speed < 0:
            raise ValueError
        self.current_speed = current_speed
        if not isinstance(count_of_seats, int):
            raise TypeError
        if count_of_seats < 0:
            raise ValueError
        self.count_of_seats = count_of_seats

    def stop(self) -> None:
        """
        Функция уменьшает скорость до 0

        Примеры:
        >>> my_car = Car("Audi", 120, 5)
        >>> my_car.stop()
        """
        ...

    def can_accommodate(self, count_of_people: int) -> bool:
        """
        Функция проверяет, вместятся ли люди в машину

        :param count_of_people: Количество людей, которые хотят вместиться в машину

        :raise ValueError: Количество людей должно быть неотрицательным числом

        :return: Вместятся ли люди в машину
        Примеры:
        >>> my_car = Car("Audi", 120, 5)
        >>> my_car.can_accommodate(7)
        """
        if not isinstance(count_of_people, int):
            raise TypeError("Количество людей должно быть типа int")
        if count_of_people < 0:
            raise ValueError("Количество людей должно быть неотрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
