from fastapi import APIRouter, Form, HTTPException
from sqlalchemy.future import select
from database import SessionDep
from models import CredsModel
from schemas import CredsSchema
from auth.security import hash_password, verify_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def add_user(user: CredsSchema, session: SessionDep) -> CredsSchema:
    new_user = CredsModel(
        login=user.login,
        password=hash_password(user.password),
    )
    session.add(new_user)
    await session.commit()
    return user

@router.post("/login-form")
async def login_form(
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    user = await session.execute(select(CredsModel).where(CredsModel.login == username))
    user = user.scalar_one_or_none()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
