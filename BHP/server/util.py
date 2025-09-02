import pickle
import json
import numpy as np
import os

# -------------------------------
# Paths to artifacts
# -------------------------------
BASE_DIR = os.path.dirname(__file__)  # server folder

# Try first: artifacts inside server/artifacts
MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "decision_tree_model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "artifacts", "columns.json")

# If not found, fallback: ../model/
if not os.path.exists(MODEL_PATH) or not os.path.exists(COLUMNS_PATH):
    MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "decision_tree_model.pkl")
    COLUMNS_PATH = os.path.join(BASE_DIR, "..", "model", "columns.json")

# -------------------------------
# Global variables
# -------------------------------
model = None
data_columns = None
locations = None

# -------------------------------
# Load saved artifacts
# -------------------------------
def load_saved_artifacts():
    global model, data_columns, locations
    print("Loading model and columns...")

    if not os.path.exists(MODEL_PATH) or not os.path.exists(COLUMNS_PATH):
        raise FileNotFoundError(f"Model or columns file not found!\nMODEL_PATH: {MODEL_PATH}\nCOLUMNS_PATH: {COLUMNS_PATH}")

    # Load trained Decision Tree model
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    # Load columns (including location names)
    with open(COLUMNS_PATH, "r") as f:
        data_columns = json.load(f)['data_columns']

    # Extract location names (all columns except first 3: total_sqft, bath, bhk)
    locations = data_columns[3:]
    print("Artifacts loaded successfully.")

# -------------------------------
# Return location names
# -------------------------------
def get_location_names():
    if locations is None:
        return []
    return locations

# -------------------------------
# Predict home price
# -------------------------------
def get_estimated_price(location, total_sqft, bhk, bath):
    if model is None or data_columns is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")

    # Find location index (if exists)
    try:
        loc_index = data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # Location not found

    # Create input array
    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    # Predict and return price
    return model.predict([x])[0]

# -------------------------------
# Test block
# -------------------------------
if __name__ == "__main__":
    load_saved_artifacts()
    print("Locations:", get_location_names())
    sample_price = get_estimated_price("Indira Nagar", 1000, 3, 2)
    print("Sample predicted price:", round(sample_price, 2))
