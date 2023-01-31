import uuid
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.forms import UserLoginForm, UserCreateForm
from app.models import connect_db, User, AuthToken
from app.utils import get_password_hash

router = APIRouter()


@router.post("/login")
async def login(user_form: UserLoginForm = Body(..., embed=True),
                database=Depends(connect_db)):
    user = database.query(User).filter(User.email == user_form.email).one_or_none()
    if user is None or get_password_hash(user_form.password) != user.password:
        return {"error": "Email/password invalid"}
    token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    database.add(token)
    database.commit()
    return {"status": "OK"}


@router.post("/user", name="user:create")
async def create_user(user: UserCreateForm,
                      database=Depends(connect_db)):
    _user = database.query(User).filter(User.email == user.email).one_or_none()
    if _user is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Already exist")

    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
    )
    database.add(new_user)
    database.commit()
    return {"user_id": new_user.id}
