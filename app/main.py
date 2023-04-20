from fastapi import FastAPI
from app.db.init_db import engine
from app.db import models
# TODO: Don't leave this here
from app.routers.temp_router import router as temp_router
from app.routers.router_sensor import router as sensor_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensor_router)
