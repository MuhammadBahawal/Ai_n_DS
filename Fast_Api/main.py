from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


@app.post("/tutor")
def tutor():
    return{
    "name":"Ahmad",
    "RollNo":239
    }


@app.post("/tutor/{id}")
def root_data(id):
    return{
        "Rollno":id
    }



@app.get("/student")
def root():
    return{
        "message":"hello",
        "name":"Ahmad",
    }
@app.post("/")
def university():
    return{
        "name":"Ali",
        "class":"BSSE",
        "RollNo":"FSD-FL-239"
    }




# path parametr

@app.post("/user{id}")
def root_app(id):
    return {
    "name":"Bahawal",
    "roll":id
    }


# qurery parameter

@app.get("/hello/{id}")
def hello(id,Name:str,depart:str,rollno:int):
    return{
        "id":id,
        "name":Name,
        "Department":depart,
        "RollNo":rollno
    }


@app.post("/admin")
def postadmin(userName:str,RollNo:str):
    try:
        return{
            "status": "success",
            "data":{
            "username":userName,
            "RollNo":RollNo
            }
    }
    except Exception as e:
        return {
            "message":str(e),
            "status":"erroe",
            "data":None
        }


# request body

class item (BaseModel):
    id:int
    name:str
    Roll :int
@app.post("/item1")
def itme(items:item):
    return items


class student(BaseModel):
    id:int
    Name:str
    RollNo:int
@app.post("/student1")
def student1(student:student):
    return student

# for get
@app.post("/")
def getStudent(student:student):
    try:return student
    except Exception as e:
        return {"message":str(e)}




