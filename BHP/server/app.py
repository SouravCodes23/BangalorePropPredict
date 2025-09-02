from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import util  # your utility file

# Create FastAPI app
app = FastAPI()

# Allow all origins for CORS (like Flask headers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input schema for prediction
class Property(BaseModel):
    location: str
    total_sqft: float
    bhk: int
    bath: int

# Route to get location names
@app.get("/get_location_names")
def get_location_names():
    locations = util.get_location_names()
    return {"locations": locations}

# Route to predict home price
@app.post("/predict_home_price")
def predict_home_price(
    location: str = Form(...),
    total_sqft: float = Form(...),
    bhk: int = Form(...),
    bath: int = Form(...)
):
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    return {"estimated_price": estimated_price}

# Startup event to load artifacts
@app.on_event("startup")
def load_artifacts():
    print("Loading saved artifacts...")
    util.load_saved_artifacts()

