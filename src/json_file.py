import json
import os

from src.contact import Contact


class JsonFile:
    def __init__(self, file_name: str = 'phonebook.json') -> None:
        self.file_name = file_name
        self.db: list = []
        self.check_file()
        self.load()

    def check_file(self) -> None:
        """Проверка файла на существование"""
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as w_file:
                json.dump([], w_file, indent=2)

    def load(self) -> None:
        with open(self.file_name, 'r', encoding='utf-8') as rfile:
            data = rfile.read()
            if not data == '':
                json_data = json.loads(data)
                for contact in json_data:
                    self.db.append(Contact(**contact))

    def save(self, data: dict) -> None:
        with open(self.file_name, 'r', encoding='utf-8') as rfile:
            text = rfile.read()
            if not text == '':
                old_data = json.loads(text)
            else:
                old_data = []
        old_data.append(data)
        with open(self.file_name, 'w', encoding='utf-8') as w_file:
            json.dump(old_data, w_file, indent=2, ensure_ascii=False)

    def save_db_to_file(self) -> None:
        data = []
        for contact in self.db:
            data.append({
                "last_name": contact.last_name,
                "first_name": contact.first_name,
                "patronymic": contact.patronymic,
                "organization_name": contact.organization_name,
                "business_phone": contact.business_phone,
                "personal_phone": contact.personal_phone
            })
        with open(self.file_name, 'w', encoding='utf-8') as w_file:
            json.dump(data, w_file, indent=2, ensure_ascii=False)
