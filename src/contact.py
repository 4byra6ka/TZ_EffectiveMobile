class Contact:

    def __init__(self, last_name: str, first_name: str, patronymic: str, organization_name: str, business_phone: str,
                 personal_phone: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.organization_name = organization_name
        self.business_phone = business_phone
        self.personal_phone = personal_phone

    def __srt__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __repr__(self):
        return (f"{self.last_name} {self.first_name} {self.patronymic} {self.organization_name} {self.business_phone} "
                f"{self.personal_phone}")
