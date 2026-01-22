
# print("Hii")

from typing import List, Dict, Optional, Annotated
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator

# Pydantic validates both types and formats.

NameField = Annotated[
    str,
    Field(
        default="Sabana",
        min_length=2,
        max_length=50,
        title="Name Field",
        description="Name of the patient",
        examples=["Sabana", "Rohit"],
    ),
]

class Patient(BaseModel):
    id: int
    name: NameField
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(default=0, gt=-1, lt=120)
    married: Optional[bool] = None
    url: AnyUrl
    allergies: List[str]
    contact_details: Dict[str, str]
    weight: float = Field(gt=0, strict=True)

    # Allow only email domains that contain 'hdfc' or 'icici'
    @model_validator(mode="after")    
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
        
         


patient_info = {
    "id": 1,
    "name": "Sabana",
    "age":70,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "email": "sabana@gainwell.com",
        "phone": "9876543210",
    },
    "url": "http://linkedin.com/in/sabana",
    "weight": 55.55,
    "email":"sabana@hdfc.com"
    # Try with: "email": "user@hdfcbank.com" or "user@icici.com"
    # "email": "user@icici.com",
}

patient1 = Patient(**patient_info)

print(patient1)

def print_patient(patient: Patient):
    print("\nPatient Details:")
    print(f"ID: {patient.id} or {patient.dict().get('id')}")
    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"Age: {patient.age}")
    print(f"Married: {patient.married}")
    print(f"URL: {patient.url}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {patient.contact_details}")
    print(f"Weight: {patient.weight}")

print_patient(patient1)
