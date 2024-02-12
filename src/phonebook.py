from src.contact import Contact
from src.json_file import JsonFile


class Phonebook(JsonFile):
    def __init__(self) -> None:
        """ Инициализация класса Phonebook и JsonFile """
        super().__init__()

    @property
    def view(self) -> list:
        """ Получение всего списка контактов из класса"""
        return self.db

    def add(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
            personal_phone: str) -> None:
        """ Добавление контакта"""
        new_contact = Contact(last_name, first_name, patronymic, organization_name, business_phone, personal_phone)
        self.db.append(new_contact)

        self.save(
            {
                "last_name": new_contact.last_name,
                "first_name": new_contact.first_name,
                "patronymic": new_contact.patronymic,
                "organization_name": new_contact.organization_name,
                "business_phone": new_contact.business_phone,
                "personal_phone": new_contact.personal_phone
            }
        )

    def delete(self, position_contact: int) -> str:
        """ Удаление контакта"""
        return f"Удален контакт {self.db.pop(position_contact)}"

    def edit(self, position_contact: int) -> Contact:
        """ Получение экземпляра класса для дальнейшего изменения контакта """
        return self.db[position_contact]

    def search(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
            personal_phone: str) -> list:
        """ Поиск по всем параметрам из базы данных """
        list_search = []
        for contact in self.db:
            if last_name != '':
                if not str(contact.last_name).lower().find(last_name.lower()):
                    list_search.append(contact)
                    break
            if first_name != '':
                if not str(contact.first_name).lower().find(first_name.lower()):
                    list_search.append(contact)
                    break
            if patronymic != '':
                if not str(contact.patronymic).lower().find(patronymic.lower()):
                    list_search.append(contact)
                    break
            if organization_name != '':
                if not str(contact.organization_name).lower().find(organization_name.lower()):
                    list_search.append(contact)
                    break
            if business_phone != '':
                if not str(contact.business_phone).lower().find(business_phone.lower()):
                    list_search.append(contact)
                    break
            if personal_phone != '':
                if not str(contact.personal_phone).lower().find(personal_phone.lower()):
                    list_search.append(contact)
                    break
        return list_search
