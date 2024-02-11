import os

from src.phonebook import Phonebook


def user_interaction():
    print("Телефонный справочник\n")
    pb = Phonebook()
    # pb.add("Grishanov", "andrey", "Urevich", "tpk", "+7495158745", "+79687310767")
    # pb.add("test", "test", "test", "test", "+test", "+test")
    while True:
        text_menu_query = {
            1: "Вывод записей из справочника",
            2: "Добавить новый контакт",
            3: "Поиск контакта",
            4: "Выход",
        }
        text_posmenu_query = {
            1: "Изменить",
            2: "Удалить",
            3: "Выход",
            "Enter": "Продолжить",
        }
        [print(f"{number_item}: {query_item}") for number_item, query_item in text_menu_query.items()]
        position_nam = input("Введи номер:")
        try:
            if int(position_nam) == 1:
                index = 0
                for contact in pb.view:
                    print(f"{'*'*100}\n{index + 1}: {contact}")
                    index += 1
                    if len(pb.view) == index or index % 10 == 0:
                        print(f"{'*' * 100}\n")
                        [print(f"{number_item}: {query_item}") for number_item, query_item in text_posmenu_query.items()]
                        position_posmenu_nam = input("Введи значение:")
                        if position_posmenu_nam == "1":
                            edit_contact = pb.edit(int(input("Введите позицию для изменения:")) - 1)
                            print(edit_contact)
                            edit_contact.last_name = input(f"Изменить значение {edit_contact.last_name} на:")
                            edit_contact.first_name = input(f"Изменить значение {edit_contact.first_name} на:")
                            edit_contact.patronymic = input(f"Изменить значение {edit_contact.patronymic} на:")
                            edit_contact.organization_name = input(f"Изменить значение {edit_contact.organization_name} на:")
                            edit_contact.business_phone = input(f"Изменить значение {edit_contact.business_phone} на:")
                            edit_contact.personal_phone = input(f"Изменить значение {edit_contact.personal_phone} на:")
                            pb.save_db_to_file()
                            print("Контакт изменён")
                        elif position_posmenu_nam == "2":
                            print(pb.delete(int(input("Введите позицию для удаления:")) - 1))
                        elif position_posmenu_nam == "3":
                            break
                print("\n")
                continue
            elif int(position_nam) == 2:
                last_name = input("Введи фамилию:")
                first_name = input("Введи имя:")
                patronymic = input("Введи отчество:")
                organization_name = input("Введи название организации:")
                business_phone = input("Введи телефон рабочий:")
                personal_phone = input("Введи телефон личный (сотовый):")
                pb.add(last_name, first_name, patronymic, organization_name, business_phone, personal_phone)
                print("\nКонтакт добавлен\n")
                continue
            elif int(position_nam) == 3:
                pass
                continue
            if int(position_nam) == 4:
                break
        except ValueError:
            print('Введите число.\n')
            continue


if __name__ == "__main__":
    user_interaction()
