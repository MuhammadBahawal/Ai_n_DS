from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/PersonalData/{name}/Fathername/{fName}/DOB/{dob}/Gender/{gender}/Mail/{mail}")
def pData(name: str, fName: str, dob: str, gender: str, mail: str):
    try:
        if not name or not fName or not dob or not gender or not mail:
            return {"error": "All fields (name, father name, DOB, gender, and mailing address) must be provided."}

        if gender.lower() not in ["male", "female"]:
            return {"error": "Gender must be 'male' or 'female'."}

        if not mail.endswith("@gmail.com"):
            return {"error": "Mailing address must be a valid Gmail address (e.g., example@gmail.com)."}

        return {
            "Name": name,
            "Father_Name": fName,
            "Date_of_Birth": dob,
            "Gender": gender.capitalize(),
            "Mailing_Address": mail
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


@app.post("/address")
def address(Province: str, district: str, address: str):
    try:
        if not Province or not district or not address:
            return {
                "error": "All fields required: Division, District, and Address."
            }
        else:
            return {
                "Division": Province,
                "District": district,
                "Address": address,
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


class PersonalData(BaseModel):
    religion: str
    nationality: str
    phone_number: str  
    email_address: str
    CNIC_number: str  
    blood_group: str
    occupation: str
    status: str
    course_name: str


@app.post("/submit-form")
def submit_form(data: PersonalData):
    try:
        if len(data.phone_number) != 11 or not data.phone_number.isdigit():
            return {"error": "Phone number must be exactly 11 digits."}

        if "@gmail.com" not in data.email_address.lower():
            return {"error": "Email address must be a valid Gmail address."}

        valid_blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        if data.blood_group not in valid_blood_groups:
            return {"error": "Blood group is not valid. Please provide a valid blood group."}

        if data.status not in ["Single", "Married"]:
            return {"error": "Status must be either 'Single' or 'Married'."}

        return {
            "message": "Form submitted successfully!",
            "data": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
