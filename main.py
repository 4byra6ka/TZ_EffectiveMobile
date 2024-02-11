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
        print(text_menu_query)
        position_nam = input("Введи номер:")
        try:
            if int(position_nam) == 1:
                pass
                continue
            elif int(position_nam) == 2:
                pass
                continue
            elif int(position_nam) == 2:
                pass
                continue
            if int(position_nam) == 4:
                break
        except ValueError:
            print('Введите число.')
            continue


if __name__ == "__main__":
    user_interaction()
