from pydantic import BaseModel, Field

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
    currency: str = Field(exclude=True)
    gross: bool = Field(exclude=True)
   

class Incoming_contacts(BaseModel):
    name: str = Field(alias='fullName')
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
    salary_range: Salary
    schedule: Schedule
 