from pydantic import BaseModel


class MeasurementIn(BaseModel):
    name: str
    value: float
    type: str

    class Config:
        orm_mode = True


class Measurement(MeasurementIn):
    timestamp: int


class Sensor(BaseModel):
    name: str
    block: str
    type: str
    status_code: int

    class Config:
        orm_mode = True


class SensorExtended(Sensor):
    measurements: list[Measurement]


class Error(BaseModel):
    name: str
    status_code: int
    timestamp: int

    class Config:
        orm_mode = True


class ErrorDb(Error):
    id: int
