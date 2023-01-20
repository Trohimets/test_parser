from pydantic import BaseModel, validator, Field
import json
from data import data, result


class Address(BaseModel):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float
    lng: float
    

class Salary(BaseModel):
    till: int = Field(alias='from')
    to: int
    currency: str
    gross: bool


class Contacts(BaseModel):
    full_name: str = Field(alias='fullName')
    phone: str
    email: str

  
class Incoming_data(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Contacts

 
incoming_data = Incoming_data.parse_raw(data)
print(incoming_data)



