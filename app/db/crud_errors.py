from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.models import Errors


def crud_get_all_errors(db: Session):
    result = db.query(Errors).all()
    if len(result) == 0:
        raise HTTPException(detail='Errors not found in database', status_code=status.HTTP_404_NOT_FOUND)
    return result


def crud_get_error_by_name(db: Session, name: str):
    result = db.query(Errors).filter(Errors.name == name).all()
    if len(result) == 0:
        raise HTTPException(detail=f'Errors for sensor not found. Name: {name}', status_code=status.HTTP_404_NOT_FOUND)
    return result
