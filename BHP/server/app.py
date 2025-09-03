from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from . import util  # relative import for util.py
from contextlib import asynccontextmanager
import os

# -------------------------------
# Lifespan: load artifacts on startup
# -------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading saved artifacts...")
    util.load_saved_artifacts()
    yield
    print("Shutting down server...")

# -------------------------------
# Create FastAPI app
# -------------------------------
app = FastAPI(lifespan=lifespan)

# -------------------------------
# CORS middleware
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Serve frontend files
# -------------------------------
client_path = os.path.join(os.path.dirname(__file__), "../client")

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory=client_path), name="static")

# Serve HTML at root
@app.get("/")
def read_index():
    return FileResponse(os.path.join(client_path, "app.html"))

# -------------------------------
# Input schema for prediction
# -------------------------------
class Property(BaseModel):
    location: str
    total_sqft: float
    bhk: int
    bath: int

# -------------------------------
# API endpoints
# -------------------------------
@app.get("/get_location_names")
def get_location_names():
    locations = util.get_location_names()
    return {"locations": locations}

@app.post("/predict_home_price")
def predict_home_price(property: Property):
    estimated_price = util.get_estimated_price(
        property.location,
        property.total_sqft,
        property.bhk,
        property.bath
    )
    return {"estimated_price": round(estimated_price, 2)}
