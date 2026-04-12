from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Nullzone API", version="1.0.0")


class User(BaseModel):
    name: str
    email: str


class Order(BaseModel):
    user_id: int
    product: str
    amount: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/users")
def list_users():
    return {"users": [], "total": 0}


@app.post("/api/v1/users")
def create_user(user: User):
    return {"id": 1, "name": user.name, "email": user.email}


@app.get("/api/v1/orders")
def list_orders():
    return {"orders": [], "total": 0}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
