
false = False
true = True

def get_parsing(data):
    result = {}
    result['address'] = data['address']['value']
    result['allow_messages'] = True
    data_from_nowhere = {
                         "allow_messages": True,
                         "billing_type": "packageOrSingle",
                         "business_area": 1
                        }
    result.update(data_from_nowhere)
    contacts = data['contacts']
    result['contacts'] = contacts
    print(result)




data = {
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "employment": "fullDay",
 "address": {
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "street": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 58.593565,
   "lng": 49.672739
 },
 "name": "Junior Backend-developer",
 "salary": {
   "from": 30000,
   "to": 70000,
   "currency": "RUR",
   "gross": false
 },
 "contacts": {
   "fullName": "Журавлев Илья",
   "phone": "79536762399",
   "email": "ilya.zhuravlev@hrb.software"
 }
}

get_parsing(data)