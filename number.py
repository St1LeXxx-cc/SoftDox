import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_header():
    clear_screen()
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   █████╗")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝")
    print("=" * 54)

def get_phone_info():
    print("Введите номер телефона (включая код страны, например +1234567890):")
    phone_number = input("Номер телефона: ")

    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, "ru")
        operator = carrier.name_for_number(parsed_number, "ru")
        time_zones = timezone.time_zones_for_number(parsed_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)

        print("\nИнформация о номере:")
        print(f"- Страна: {country}")
        print(f"- Оператор связи: {operator}")
        print(f"- Временные зоны: {', '.join(time_zones)}")
        print(f"- Валидный номер: {'Да' if is_valid else 'Нет'}")
        print(f"- Возможен для звонков: {'Да' if is_possible else 'Нет'}")
    except phonenumbers.NumberParseException:
        print("Ошибка: Неверный формат номера телефона.")

def main():
    while True:
        show_header()
        print("[1] Информация о номере")
        print("[0] Выход")
        print("=" * 54)
        choice = input("Выберите опцию: ")

        if choice == "1":
            get_phone_info()
            input("\nНажмите Enter, чтобы вернуться в меню...")
        elif choice == "0":
            print("\nВыход из программы...")
            break
        else:
            print("\nНеверный ввод. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()