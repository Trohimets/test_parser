import json

from models import Phone



def write_json_to_file(data, filename):
    """Функция для записи результата 
    в json-файл"""
    data = json.loads(data)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent = 4)
    

def separate_phone(phone_number):
    """Функция разделения номера телефона 
    на код страны, города и сам номер"""
    number = f'{phone_number[-7:-4]}-{phone_number[-4:-2]}-{phone_number[-2:]}'
    city = phone_number[-10:-7]
    country = phone_number[:-10]
    phone = Phone(city=city,country=country,number=number)
    return phone