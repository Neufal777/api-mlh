from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import uuid

app = FastAPI()

users = [
    {"id": str(uuid.uuid4()),"username": "Pranav", "email": "Pranav@ghw.com", "password":"pass", "role":"admin"},
    {"id": str(uuid.uuid4()),"username": "Kosu", "email": "Kosu@ghw.com", "password":"pass", "role":"user"},
]

#Pydantic model
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str

class UserUpdate(BaseModel):
    username: str
    email: str

security = HTTPBasic()

# Check if user is authenticated
def authenticate(credentials: HTTPBasicCredentials = Security(security)):
    user = None
    for u in users:
        if u["username"] == credentials.username and u["password"] == credentials.password:
            user = u
            return user
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return None

# authorize user
def authorize(user: dict = Depends(authenticate)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Permission denied")
    return None

@app.get("/users", response_model=list[UserResponse])
def get_users(user: dict = Depends(authorize)):
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, user: dict = Depends(authorize)):
    for u in users:
        if u["id"] == user_id:
            return u
    return {"message": "User not found"}

@app.post("/users")
def create_user(user: UserResponse):
    new_user = {
        "id": str(uuid.uuid4()),
        "username": user.username,
        "email": user.email
    
    }
    users.append(new_user)
    return new_user, 201

@app.put("/users/{user_id}")
def update_user(user_id: str, user: UserResponse):
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