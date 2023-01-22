from pydantic import ValidationError

from models import (Incoming_data, Result_contacts,
                    Coordinates, Experience, Schedule,
                    Result_data)
from functions import write_json_to_file, separate_phone



def main():
    """Основная логика. Считывание файла с данными, 
    конструирование полей результирующего объекта и
    запись его в файл"""
    try:
        incoming_data = Incoming_data.parse_file('data.json')
    except ValidationError as e:
        print(e.json())
    address = incoming_data.address.value
    allow_messages = True
    billing_type = 'packageOrSingle'
    business_area = 1

    phone = separate_phone(incoming_data.contacts.phone)
    contacts = Result_contacts(email=incoming_data.contacts.email,
                            name=incoming_data.contacts.name,
                            phone=phone)
    coordinates = Coordinates(latitude=incoming_data.address.lat,
                            longitude=incoming_data.address.lng)
    description = incoming_data.description
    experience = Experience(id='noMatter')
    html_tags = True
    image_url = 'https://img.hhcdn.ru/employer-logo/3410666.jpeg'
    salary = incoming_data.salary.till
    schedule = Schedule(id='fullDay')

    result_data = Result_data(address=address, allow_messages=allow_messages,
                            billing_type=billing_type, business_area=business_area,
                            result_contacts=contacts, coordinates=coordinates,
                            description=description, experience=experience,
                            html_tags=html_tags, image_url=image_url,
                            name=incoming_data.name, salary=salary,
                            salary_range=incoming_data.salary, schedule=schedule)
    result = result_data.json(ensure_ascii=False, by_alias=True)
    write_json_to_file(result, 'result.json')
    
    
if __name__ == '__main__':
    main()