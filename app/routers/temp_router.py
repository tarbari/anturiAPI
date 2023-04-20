# TODO: DELETE THIS FILE
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.db_connection import get_db
from app.db.crud_temp import *

router = APIRouter(prefix='/temp')


@router.get('')
def get_temp(db: Session = Depends(get_db)):
    return crud_temp(db)
