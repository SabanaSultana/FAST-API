from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!", "number":910}

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
        # return data
    print("Patient data loaded.")
    print("This is out data",data)

@app.get("/patient")    
def get_patient():
    return load_patientData()

print(load_patientData())