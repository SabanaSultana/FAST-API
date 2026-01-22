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

# print("Addess Details:",  address1)
# print("patient_details:",  patient1)
# print("Patient's Name", patient1.name)
# print("Patient's City:", patient1.address.city)
# print("Patient's State:", patient1.address.state)
# print("Patient's Pin:", patient1.address.pin)   
# print("Patient's Address:", patient1.address) 


## Exporting model as dictionary
temp=patient1.model_dump()
print("Patient as dict:", temp)
print(type(temp))

## Exporting model as JSON
temp_json=patient1.model_dump_json()    
print("Patient as JSON:", temp_json)
print(type(temp_json))


## dict
di= {
    "name":"Sabana",
    "gender":"female",
    "age":20,
    "address": {
        "city":"kolkata",
        "state":"wb",
        "pin":"700156"
    }
}

print(di)

temp2=patient1.model_dump(include={'name','address'})
temp3=patient1.model_dump(exclude={'age'})

print("Included fields:", temp2)
print("Excluded fields:", temp3)

temp4 = patient1.model_dump(
    include={
        "name": True,
        "address": {"city", "pin"}
    }
)

print("Nested include:", temp4)


##  exclude unset , will exclude fields which are not set during object creation but can have default values