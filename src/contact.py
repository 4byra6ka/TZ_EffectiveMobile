class Contact:

    def __init__(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
                 personal_phone: str) -> None:
        """ Инициализация класса Contact """
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._organization_name = organization_name
        self._business_phone = business_phone
        self._personal_phone = personal_phone

    def __srt__(self) -> str:
        """ Вывод информации"""
        return (f"{'*'*100}"
                f"{self.last_name} {self.first_name} {self.patronymic} {self.organization_name} {self.business_phone}"
                f"{self.personal_phone}"
                f"{'*'*100}\n")

    def __repr__(self) -> str:
        """ Техническая информация"""
        return (f"{self.last_name} {self.first_name} {self.patronymic} {self.organization_name} {self.business_phone} "
                f"{self.personal_phone}")

    @property
    def last_name(self) -> str:
        """ Геттер для фамилии"""
        return self._last_name

    @last_name.setter
    def last_name(self, name: str) -> None:
        """ Сеттер для фамилии"""
        self._last_name = name

    @property
    def first_name(self) -> str:
        """ Геттер для имени"""
        return self._first_name

    @first_name.setter
    def first_name(self, name: str) -> None:
        """ Сеттер для имени"""
        self._first_name = name

    @property
    def patronymic(self) -> str:
        """ Геттер для отчества"""
        return self._patronymic

    @patronymic.setter
    def patronymic(self, name: str) -> None:
        """ Сеттер для отчества"""
        self._patronymic = name

    @property
    def organization_name(self) -> str:
        """ Геттер для названия организации"""
        return self._organization_name

    @organization_name.setter
    def organization_name(self, name: str) -> None:
        """ Сеттер для названия организации"""
        self._organization_name = name

    @property
    def business_phone(self) -> str:
        """ Геттер для телефона рабочий"""
        return self._business_phone

    @business_phone.setter
    def business_phone(self, phone: str) -> None:
        """ Сеттер для телефона рабочий"""
        self._business_phone = phone

    @property
    def personal_phone(self) -> str:
        """ Геттер для телефона личный (сотовый)"""
        return self._personal_phone

    @personal_phone.setter
    def personal_phone(self, phone: str) -> None:
        """ Сеттер для телефона личный (сотовый)"""
        self._personal_phone = phone
