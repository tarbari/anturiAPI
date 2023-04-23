# TODO: Needs work
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.db_connection import get_db
from app.db.schemas import ErrorIn
from app.db.crud_errors import *

router = APIRouter(prefix='/errors', tags=['Errors'])


@router.get('', status_code=status.HTTP_200_OK)
def get_all_errors(db: Session = Depends(get_db)):
    return crud_get_all_errors(db)


@router.get('/{name}', status_code=status.HTTP_200_OK)
def get_error_by_name(name: str, db: Session = Depends(get_db)):
    return crud_get_error_by_name(db, name)
