from parse_pydantic import main


 
result = {
            "address": "г Киров, ул Володарского, д 157",
            "allow_messages": true,
            "billing_type": "packageOrSingle",
            "business_area": 1,
            "contacts": {
            "email": "ilya.zhuravlev@hrb.software",
            "name": "Журавлев Илья",
            "phone": {
                "city": "953",
                "country": "7",
                "number": "676-23-99"
            }
            },
            "coordinates": {
            "latitude": 58.593565,
            "longitude": 49.672739
            },
            "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
            "experience": {
            "id": "noMatter"
            },
            "html_tags": true,
            "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
            "name": "Junior Backend-developer",
            "salary": 70000,
            "salary_range": {
            "from": 30000,
            "to": 70000
            },
            "schedule": {
            "id": "fullDay"
            }
            }


def test_get_parsing():

    assert main == result, 'Тест не выполнен. Данные не соответствуют образцу'
