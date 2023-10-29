"""
Simple FastAPI application that returns the current time in different timezones.
"""
from fastapi import FastAPI
import pendulum

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Please pass the city name to the /time endpoint!. Only European cities are supported.",
        "example": "/time/Paris"
        }

@app.get("/time/{city}")
async def get_time(city: str):
    tz = pendulum.timezone(f"Europe/{city}")
    time = pendulum.now(tz)
    return {"time": time.to_datetime_string()}
