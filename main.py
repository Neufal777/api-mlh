from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

users = [
    {"id": str(uuid.uuid4()),"username": "Pranav", "email": "Pranav@ghw.com"},
    {"id": str(uuid.uuid4()),"username": "Kosu", "email": "Kosu@ghw.com"},
]

#Pydantic model
class User(BaseModel):
    username: str
    email: str

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: str):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}

@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": str(uuid.uuid4()),
        "username": user.username,
        "email": user.email
    
    }
    users.append(new_user)
    return new_user, 201

@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    for u in users:
        if u["id"] == user_id:
            u["username"] = user.username
            u["email"] = user.email
            return u
    return {"message": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost" , port=8000)