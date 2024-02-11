from src.contact import Contact
from src.json_file import JsonFile


class Phonebook(JsonFile):
    def __init__(self):
        super().__init__()

    def view(self):
        return

    def add(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
            personal_phone: str):
        new_contact = Contact(last_name, first_name, patronymic, organization_name, business_phone, personal_phone)
        self.db.append(new_contact)
        self.save(new_contact.__dict__)

    def delete(self):
        return

    def edit(self):
        return

    def search(self):
        return
