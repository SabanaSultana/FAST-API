from fastapi import FastAPI, HTTPException as http
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional, List, Literal
import json


app=FastAPI()

## Pydantic models 
class DataItem(BaseModel):
    id:Annotated[int, Field(gt=0, lt=100, description1="Enter an patient ID", description2="ID must be between 0 and 100")]
    name:Annotated[str, Field(min_length=3, max_length=50, description="Enter patient name")]
    age:Annotated[int, Field(gt=0, lt=120, description="Enter patient age")]
    city:Optional[Annotated[str, Field(min_length=2, max_length=50, description="Enter patient city")]] =None
    gender:Literal['male', 'female', 'other']
    email:Annotated[EmailStr, Field(description="Enter patient email")]  
    phone:Annotated[str, Field(description="Enter 10 digit phone number")]
    date_of_birth:Annotated[str, Field(description="Enter date of birth in YYYY-MM-DD format")]
    blood_type:Optional[Annotated[str, Field(description="Enter blood type")]] =None
    conditions: Annotated[List[str], Field(description="List of medical conditions")]
    medications: Annotated[List[str], Field(description="List of medications")]
    last_visit:Optional[Annotated[str, Field(description="Enter last visit date in YYYY-MM-DD format")]] =None


def load_data():
    with open('patient_info.json', 'r') as f:
        data=json.load(f)
    return data

@app.post('/insert_data')

def insert_data(patient: DataItem):
    
    data=load_data()
    print("data:", data)
    print("Type of data:", type(data))
    print("Patient to insert:", patient)
    print("Type of patient:", type(patient))

    if patient.id in [item['id'] for item in data["patients"]]:
        raise http(status_code=400, detail="Patient with this ID already exists.")
    
    data["patients"].append(patient.dict()) 
    with open("patient_info.json", "w") as f:
         json.dump(data, f, indent=4) 
         return {"message": "Patient added successfully"}

    print("Patient data is valid.") 
    
