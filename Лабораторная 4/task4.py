class Property:
    """
    Базовый класс, обозначающий имущество
    """

    def __init__(self, owner: str, price: float):
        """
        Конструктор класса "имущество"

        :protected (т.к. нельзя "отобрать" что-либо у владельца) param _owner: Владелец имущества (ФИО)
        :protected (т.к. нельзя снизить цену до желаемой) _price: Цена имущества (в рублях)

        Примеры:
        >>> my_property = Property("Кукушкина Ланиакея Дмитриевна", 2000560)  # инициализация экземпляра класса
        """
        self._owner = owner
        self._price = price

    @property
    def owner(self) -> str:
        """
        Геттер показывает значение защищенного атрибута - ФИО владельца
        """
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        """
        Сеттер устанавливает новое значение защищенного атрибута - ФИО владельца

        :raise TypeError: Если ФИО не является строкой, то кидаем исключение
        """
        if isinstance(new_owner, str):
            self._owner = new_owner
        else:
            raise TypeError("Владелец должен быть указан как строка")

    @property
    def price(self) -> float:
        """
        Геттер показывает значение защищенного атрибута - цену
        """
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Сеттер устанавливает новое значение защищенного атрибута - цену

        :raise ValueError: Если цены <=0, то кидаем исключение
        :raise TypeError: Если цена не является вещественным числом, то кидаем исключение
        """
        if isinstance(new_price, float):
            if new_price > 0:
                self._price = new_price
            else:
                raise ValueError("Цена должна быть положительной")
        else:
            raise TypeError("Цена должна быть вещественным числом")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта
        """
        return f"Владелец: {self._owner}. Цена: {self._price}"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта
        """
        return f"{self.__class__.__name__}(owner={self._owner!r}, price={self._price})"

    def reset_price(self) -> None:
        """
        Функция обнуляет цену имущества

        :param additional_price: Добавляемая цена (в рублях)

        Примеры:

        >>> my_property = Property("Кукушкина Ланиакея Дмитриевна", 2000560)
        >>> my_property.reset_price()
        """
        self._price = 0

    def increase_price(self, additional_price: float) -> None:
        """
        Функция увеличивает цену имущества

        :param additional_price: Добавляемая цена (в рублях)

        :raise ValueError: Если количество добавлеяемой цены <=0, то кидаем исключение
        :raise TypeError: Если добавлеяемая цена не является вещественным числом, то кидаем исключение

        Примеры:

        >>> my_property = Property("Кукушкина Ланиакея Дмитриевна", 2000560.5)
        >>> my_property.increase_price(100000.5)
        """
        if isinstance(additional_price, float):
            if additional_price > 0:
                self._price += additional_price
            else:
                raise ValueError("Добавляемая цена должна быть положительной")
        else:
            raise TypeError("Добавляемая цена должна быть вещественным числом")


class Auto(Property):
    """
    Базовый класс, обозначающий автомобиль
    """

    def __init__(self, owner: str, price: float, brand: str):
        """
        Конструктор класса "автомобиль"

        :protected param _owner: Владелец имущества (ФИО)
        :protected _price: Цена имущества (в рублях)
        :public param brand: Марка автомобиля (название)

        Примеры:
        >>> my_auto = Auto("Кукушкина Ланиакея Дмитриевна", 2000560, "audi")  # инициализация экземпляра класса
        """
        super().__init__(owner, price)
        self.brand = brand

    def __str__(self):
        """
        Возвращает строковое представление объекта
        """
        return f"{super().__str__()} Бренд: {self.brand}"

    def __repr__(self):
        """
        Возвращает строковое объекта
        """
        return f"{super().__repr__()}, brand={self.brand!r})"

    def increase_price(self, additional_price: float) -> None:
        """
        Функция увеличивает цену автомобиля
        Перегружаем, так как цена еще больше увеличивается, если бренд - ауди

        :param additional_price: Добавляемая цена (в рублях)

        :raise ValueError: Если количество добавлеяемой цены <=0, то кидаем исключение
        :raise TypeError: Если добавлеяемая цена не является вещественным числом, то кидаем исключение
        """
        coef_for_audi = 1
        if isinstance(additional_price, float):
            if additional_price > 0:
                if self.brand == "audi":
                    coef_for_audi = 1.5
                self._price += additional_price * coef_for_audi
            else:
                raise ValueError("Добавляемая цена должна быть положительной")
        else:
            raise TypeError("Добавляемая цена должна быть вещественным числом")


class House(Property):
    """
    Базовый класс, обозначающий дом
    """

    def __init__(self, owner: str, price: float, number_of_rooms: int):
        """
        Конструктор класса "дом"

        :protected param _owner: Владелец имущества (ФИО)
        :protected _price: Цена имущества (в рублях)
        :public param number_of_rooms: Количество комнат в доме

        Примеры:
        >>> my_house = House("Кукушкина Ланиакея Дмитриевна", 2000560, 9)  # инициализация экземпляра класса
        """
        super().__init__(owner, price)
        self.number_of_rooms = number_of_rooms

    def __str__(self):
        """
        Возвращает строковое представление объекта
        """
        return f"{super().__str__()} Количество комнат: {self.number_of_rooms}"

    def __repr__(self):
        """
        Возвращает строковое объекта
        """
        return f"{super().__repr__()}, number_of_rooms={self.number_of_rooms})"

    def increase_price(self, additional_price: float) -> None:
        """
        Функция увеличивает цену дома
        Перегружаем, так как цена еще больше увеличивается в зависимости от количества комнат

        :param additional_price: Добавляемая цена (в рублях)

        :raise ValueError: Если количество добавлеяемой цены <=0, то кидаем исключение
        :raise TypeError: Если добавлеяемая цена не является вещественным числом, то кидаем исключение
        """
        if isinstance(additional_price, float):
            if additional_price > 0:
                self._price += additional_price * self.number_of_rooms
            else:
                raise ValueError("Добавляемая цена должна быть положительной")
        else:
            raise TypeError("Добавляемая цена должна быть вещественным числом")


if __name__ == "__main__":
    auto = Auto("me", 3524345, "audi")
    house = House("me", 231443.13, 7)
    print(auto)
    auto.increase_price(5)
    print(repr(auto))
    print(house)
    house.increase_price(4536.45)
    print(repr(house))
