from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'kolkata', 'state': 'wb', 'pin': '700156'}

address1 = Address(**address_dict)

patient_dict = {'name': 'sabana', 'gender': 'female', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

print("Addess Details:",  address1)
print("patient_details:",  patient1)
print("Patient's Name", patient1.name)
print("Patient's City:", patient1.address.city)
print("Patient's State:", patient1.address.state)
print("Patient's Pin:", patient1.address.pin)   
print("Patient's Address:", patient1.address) 



