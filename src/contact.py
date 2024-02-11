class Contact:

    def __init__(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
                 personal_phone: str) -> None:
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._organization_name = organization_name
        self._business_phone = business_phone
        self._personal_phone = personal_phone

    def __srt__(self):
        return (f"{'*'*100}"
                f"{self.last_name} {self.first_name} {self.patronymic} {self.organization_name} {self.business_phone}"
                f"{self.personal_phone}"
                f"{'*'*100}\n")

    def __repr__(self) -> str:
        return (f"{self.last_name} {self.first_name} {self.patronymic} {self.organization_name} {self.business_phone} "
                f"{self.personal_phone}")

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, name: str) -> None:
        self._last_name = name

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, name: str) -> None:
        self._first_name = name

    @property
    def patronymic(self) -> str:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, name: str) -> None:
        self._patronymic = name

    @property
    def organization_name(self) -> str:
        return self._organization_name

    @organization_name.setter
    def organization_name(self, name: str) -> None:
        self._organization_name = name

    @property
    def business_phone(self) -> str:
        return self._business_phone

    @business_phone.setter
    def business_phone(self, phone: str) -> None:
        self._business_phone = phone

    @property
    def personal_phone(self) -> str:
        return self._personal_phone

    @personal_phone.setter
    def personal_phone(self, phone: str) -> None:
        self._personal_phone = phone
