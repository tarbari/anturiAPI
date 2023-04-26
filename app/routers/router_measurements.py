from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.db_connection import get_db
from app.db.schemas import MeasurementIn, Measurement
from app.db.crud_measurements import *

router = APIRouter(prefix='/measurements', tags=['Measurements'])


@router.post('', status_code=status.HTTP_201_CREATED)
def create_new_measurement(measurement: MeasurementIn, db: Session = Depends(get_db)):
    crud_create_measurement(db, measurement)


@router.delete('', status_code=status.HTTP_204_NO_CONTENT)
def delete_measurements(name: str, timestamp: int, db: Session = Depends(get_db)):
    crud_delete_measurement(db, name, timestamp)


# TODO: Remove this before returning
@router.get('', status_code=status.HTTP_200_OK, response_model=list[Measurement])
def get_all_measurements(db: Session = Depends(get_db)):
    return crud_read_all_measurements(db)
