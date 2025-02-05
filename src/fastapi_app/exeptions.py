from fastapi.exceptions import HTTPException
from fastapi import status


incorrect_username_or_password = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Basic"},
)


user_already_exist = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="user or email already exist"
)

user_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='user not found'
)

task_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='task not found or already closed'
)