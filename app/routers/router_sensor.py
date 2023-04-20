from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.db_connection import get_db
from app.db.crud_sensor import *
from app.db.schemas import Sensor

router = APIRouter(prefix='/sensors', tags=['Sensors'])


@router.get('', response_model=list[Sensor])
def get_sensors(db: Session = Depends(get_db)):
    return read_all_sensors(db)


@router.put('', response_model=Sensor, status_code=status.HTTP_201_CREATED)
def add_sensor(sensor: Sensor, db: Session = Depends(get_db)):
    return create_sensor(db, sensor)


# TODO: Remove this before returning
@router.delete('/{name}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sensor(name: str, db: Session = Depends(get_db)):
    result = destroy_sensor(db, name)
    if result == 0:
        raise HTTPException(detail='Sensor not found', status_code=status.HTTP_404_NOT_FOUND)
