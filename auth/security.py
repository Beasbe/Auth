from passlib.context import CryptContext
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import APIRouter, Depends
from typing import Annotated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.get("/protected-basic")
def authenticate_basic(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {"message": f"Hello, {credentials.username}! Basic authentication successful."}
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
