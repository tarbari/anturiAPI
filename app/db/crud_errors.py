# TODO: Needs work
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.schemas import ErrorIn
from app.db.models import Error


def crud_get_all_errors(db: Session, error: ErrorIn):
    return 0


def crud_get_error_by_name(db: Session, name: str):
    result = db.query(Error).filter(Error.name == name).all()
    if len(result) == 0:
        raise HTTPException(detail='Sensor not found ¯\_(ツ)_/¯', status_code=status.HTTP_404_NOT_FOUND)
