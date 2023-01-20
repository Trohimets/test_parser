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


class Incoming_contacts(BaseModel):
    full_name: str = Field(alias='fullName')
    phone: str
    email: str

  
class Incoming_data(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Incoming_contacts


class Phone(BaseModel):
    city: str
    country: str
    number: str


class Result_contacts(BaseModel):
    email: str
    name: str
    phone: Phone


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Experience(BaseModel):
    id: str


class Salary_range(BaseModel):
    till: int = Field(alias='from')
    to: int


class Schedule(BaseModel):
    id: str

class Result_data(BaseModel):
    address: str
    allow_messages: bool
    billing_type: str
    business_area: int
    result_contacts: Result_contacts
    coordinates: Coordinates
    description: str
    experience: Experience
    html_tags: bool
    image_url: str
    name: str
    salary: int
    salary_range: Salary_range
    schedule: Schedule
 


incoming_data = Incoming_data.parse_raw(data)
result_data = Result_data.
print(incoming_data)



