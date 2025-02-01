from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define Pydantic models for body validation
class RegisterStudentModel(BaseModel):
    name: str
    email: str
    age: int
    courses: List[str]

class UpdateEmailModel(BaseModel):
    email: str


# GET /students/{student_id}
@app.get("/students/{student_id}")
def get_student(student_id: int, include_grades: bool = False, semester: str = None):
    # Validate student_id (manually)
    if student_id < 1001 or student_id > 9998:
        return {"message": "student_id must be between 1001 and 9998"}

    # Validate semester format (manually)
    if semester and semester not in ["Fall2024", "Spring2025", "Summer2025"]:
        return {
            "message": "Invalid semester format. Please use Fall2024, Spring2025, etc."
        }

    return {
        "student_id": student_id,
        "include_grades": include_grades,
        "semester": semester if semester else "Not specified",
    }


# POST /students/register
@app.post("/students/register")
def register_student(student: RegisterStudentModel):
    # Validate name (only alphabets and spaces manually)
    if not student.name.isalpha() and not all(c.isalpha() or c.isspace() for c in student.name):
        return {"message": "Name should contain only alphabets and spaces."}

    # Validate email (basic check for '@' and '.')
    if "@" not in student.email or "." not in student.email:
        return {"message": "Invalid email format."}

    # Validate age (must be between 18 and 30)
    if student.age < 18 or student.age > 30:
        return {"message": "Age must be between 18 and 30."}

    # Validate courses (1 to 5 courses, each between 5-30 characters)
    if len(student.courses) < 1 or len(student.courses) > 5:
        return {"message": "Courses must be between 1 and 5."}
    
    for course in student.courses:
        if len(course) < 5 or len(course) > 30:
            return {"message": "Each course name must be between 5 and 30 characters."}

    # Check for duplicate course names
    if len(student.courses) != len(set(student.courses)):
        return {"message": "Duplicate course names are not allowed."}

    return {"message": "Student registered successfully!"}


# PUT /students/{student_id}/email
@app.put("/students/{student_id}/email")
def update_email(student_id: int, student: UpdateEmailModel):
    # Validate student_id (manually)
    if student_id < 1001 or student_id > 9999:
        return {"message": "student_id must be between 1001 and 9999."}

    # Validate email (basic check for '@' and '.')
    if "@" not in student.email or "." not in student.email:
        return {"message": "Invalid email format."}

    return {"student_id": student_id, "email": student.email, "message": "Email updated successfully!"}
