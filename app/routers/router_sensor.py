from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.db_connection import get_db
from app.db.crud_sensor import crud_read_all_sensors, crud_read_sensor_by_name, crud_create_sensor, \
    crud_update_sensor_status, crud_read_sensor_by_status, \
    crud_update_sensor_block, crud_destroy_sensor, crud_read_sensors_by_block
from app.db.schemas import Sensor, SensorExtended

router = APIRouter(prefix='/sensors', tags=['Sensors'])


@router.get('', response_model=list[Sensor])
def get_sensors(db: Session = Depends(get_db)):
    return crud_read_all_sensors(db)


@router.post('', response_model=Sensor, status_code=status.HTTP_201_CREATED)
def create_new_sensor(sensor: Sensor, db: Session = Depends(get_db)):
    return crud_create_sensor(db, sensor)


@router.put('/{name}/status_code', response_model=Sensor)
def update_sensor_status_code(name: str, status_code: int, db: Session = Depends(get_db)):
    return crud_update_sensor_status(db, name, status_code)


@router.put('/{name}/block', status_code=status.HTTP_204_NO_CONTENT)
def update_sensor_block(name: str, block: str, db: Session = Depends(get_db)):
    result = crud_update_sensor_block(db, name, block)
    if result == 0:
        raise HTTPException(detail='Sensor not found', status_code=status.HTTP_404_NOT_FOUND)


@router.get('/{name}', response_model=SensorExtended)
def get_sensor_by_name(name: str, start_time: int = 0, end_time: int = 0, db: Session = Depends(get_db)):
    return crud_read_sensor_by_name(db, name, start_time, end_time)


@router.get('/status_code/{status_code}', response_model=list[Sensor])
def get_sensor_by_status_code(status_code: int, db: Session = Depends(get_db)):
    result = crud_read_sensor_by_status(db, status_code)
    return result


@router.get('/block/{block}', response_model=list[Sensor])
def get_sensors_by_block(block: str, db: Session = Depends(get_db)):
    return crud_read_sensors_by_block(db, block)


# TODO: Remove this before returning
@router.delete('/{name}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sensor(name: str, db: Session = Depends(get_db)):
    result = crud_destroy_sensor(db, name)
    if result == 0:
        raise HTTPException(detail='Sensor not found', status_code=status.HTTP_404_NOT_FOUND)
