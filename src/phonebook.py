from src.contact import Contact
from src.json_file import JsonFile


class Phonebook(JsonFile):
    def __init__(self):
        super().__init__()

    @property
    def view(self) -> list:
        return self.db

    def add(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
            personal_phone: str) -> None:
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
        return f"Удален контакт {self.db.pop(position_contact)}"

    def edit(self, position_contact: int) -> Contact:
        return self.db[position_contact]

    def search(self):
        return
