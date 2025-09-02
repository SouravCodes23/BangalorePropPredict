from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import util  # your utility file
from contextlib import asynccontextmanager

# -------------------------------
# Input schema for prediction
# -------------------------------
class Property(BaseModel):
    location: str
    total_sqft: float
    bhk: int
    bath: int

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
# Routes
# -------------------------------

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running!"}

@app.get("/get_location_names")
def get_location_names():
    """Return list of locations for frontend dropdown"""
    locations = util.get_location_names()
    return {"locations": locations}

@app.post("/predict_home_price")
def predict_home_price(property: Property):
    """Predict home price given input data"""
    estimated_price = util.get_estimated_price(
        property.location,
        property.total_sqft,
        property.bhk,
        property.bath
    )
    return {"estimated_price": round(estimated_price, 2)}
