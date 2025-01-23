from fastapi import FastAPI

app = FastAPI()

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



