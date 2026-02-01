from sqlmodel import Session, select
from src.users.models import User
from src.users.schemas import UserCreate, UserUpdate


# CREATE USER
def create_user(session: Session, user_data: UserCreate):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# GET ALL USERS
def get_users(session: Session):
    statement = select(User)
    return session.exec(statement).all()


# UPDATE USER
def update_user(session: Session, user_id, user_data: UserUpdate):
    user = session.get(User, user_id)
    if not user:
        return None

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# DELETE USER
def delete_user(session: Session, user_id):
    user = session.get(User, user_id)
    if not user:
        return False

    session.delete(user)
    session.commit()
    return True
