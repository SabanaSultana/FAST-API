
# print("Hii")

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict,Optional, Annotated

##  Pydantic is use to validate both type and format of data

class Patient(BaseModel):
    id: int
    # name: str
    name:Annotated [str, Field(default="Sabana", min_length=2, max_length=50, title="Name Field", description="Name of the patient", examples=["Sabana", 'Rohit'])]  # Custom validation using Field, name must be between 2 and 50 characters, Together Annotated and Field can be used to add metadata to the field
    email:Optional[EmailStr]=None # Pydantic will validate that the email is in a proper format, EmailStr is a custom data type provided by pydantic, if email is optional and no default value is provided then pydantic will consider it as required field
    age: Optional[int] = Field(default=0, gt=-1, lt=120) # Default age is 0 if not provided
    married: Optional[bool]= None
    url:AnyUrl  # Pydantic will validate that the URL is in a proper format, AnyUrl is a custom type provided by pydantic
    allergies: List[str]
    contact_details: Dict[str, str]   ## why not dict(), because we want to specify key and value types explicitly. Contact details is a dictionary with string keys and string values (Two level valiation)
    weight: float= Field(gt=0, strict=True)  # Weight must be greater than 0, your custom data validation using Field provided by pydantic, strict ensures that the value must be of type float, not int or str (prohibits implicit type conversion by pydantic)


patient_info = {
    "id": 1,
    "name": "Sabana",
    "age": 12,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "email": "sabana@gainwell.com",
        "phone": "9876543210" #-- (If phone number is int, pydantic will raise a validation error because it expects a string )
    },
    "url": "http://linkedin.com/in/sabana",
    "weight": 55.55  # "weight": "55.5"
}

patient1 = Patient(**patient_info)

print(patient1)

def print_patient(patient: Patient):
    print("\nPatient Details:")
    print(f"ID: {patient.id} or {patient.dict().get('id')}")
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {patient.contact_details}")

print_patient(patient1)
