from fastapi import FastAPI
from app.db.initialize_database import engine
from app.db import models
from app.routers.router_sensor import router as sensor_router
from app.routers.router_measurements import router as measurements_router
from app.routers.router_errors import router as errors_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensor_router)
app.include_router(measurements_router)
app.include_router(errors_router)
