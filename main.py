from fastapi import FastAPI, Path
import json
from fastapi import HTTPException as http 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!", "number":910000}

def additional_function():
    return "This is an additional function." # This function does not include a route decorator and will not be exposed as an endpoint.

#Each function defined with a route decorator (like @app.get) will be exposed as an endpoint in the FastAPI application.

print(additional_function())  # Calling the additional function, but it won't be an endpoint.

@app.get("/about")
def about():
    return {"message": "This is the about page.", "number":2}


def load_patientData():
    with open('patient_info.json', 'r') as file:
        data=json.load(file)
        return data
    print("Patient data loaded.")
    print("This is out data",data)

@app.get("/patient")    
def get_patient():
    return load_patientData()

# print(load_patientData())


## Parameterized Endpoint to get patient by ID

@app.get("/patient/{patient_id}")
def get_patient_by_id(patient_id:int =Path(..., description="The ID of the patient to retrieve", example=1)):
    data=load_patientData()
    print("Data in get_patient_by_id:",data)
    patients=data['patients']
    print("Patient data:",patients)
    for patient in patients:
        if patient['id']==patient_id:
            print("Patient found:",patient)
            return patient
        
    # return {"message": "Patient not found"}
    raise http(status_code=404, detail="Patient not found")


## Query paramater to sort by age descending

@app.get("/patients_sorted")
def get_patients_sorted_by_age(sort : str=None):
    data=load_patientData()
    patient=data['patients']
    if sort =="desc":
        sorted_patients=sorted(patient, key= lambda x:x['age'], reverse=True)
        return {"patients": sorted_patients}
    else:
        return {"patients": patient}
    
# Example usage: /patients_sorted?sort=desc to get patients sorted by age in descending order