from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store passwords in memory (You can use a database for persistent storage)
password_data = {"old_password": "", "new_password": ""}

# Pydantic Model for Request Body
class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str

# Route to update password variables from Flutter
@app.post("/update_password")
def update_password(data: PasswordUpdate):
    password_data["old_password"] = data.old_password
    password_data["new_password"] = data.new_password
    return {"message": "Password updated successfully!"}

# Route to fetch current password values
@app.get("/get_passwords")
def get_passwords():
    return password_data

