Perfect! Here’s a **ready-to-use `README.md` template** for your Upper Bengaluru House Price Prediction project:
Live Demo:[text](https://bangaloreproppredict-4.onrender.com/)

---

# Upper Bengaluru House Price Prediction

This project is a **machine learning-based web API** to predict house prices in Upper Bengaluru. It uses a **Decision Tree Regressor** model and a **FastAPI backend**.

---

## **Project Structure**

```
Real-Estate-Price-Prediction/
│
├── BHP/
│   ├── client/                <-- Frontend (optional)
│   ├── server/                <-- FastAPI backend
│   │   ├── app.py             <-- FastAPI application
│   │   ├── util.py            <-- ML utilities
│   │   └── artifacts/         <-- Trained model & JSON columns
│   │       ├── decision_tree_model.pkl
│   │       └── columns.json
│   └── model/                 <-- ML training scripts or notebooks
├── .gitignore
├── requirements.txt
└── README.md
```

---

## **Setup Instructions**

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/real-estate-price-prediction.git
cd real-estate-price-prediction
```

### **2. Create a virtual environment**

```bash
python -m venv venv
```

### **3. Activate the virtual environment**

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### **4. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **Running the FastAPI Backend**

1. Navigate to the server folder:

```bash
cd BHP/server
```

2. Start the server using **uvicorn**:

```bash
uvicorn app:app --reload
```

* The backend will be available at: `http://127.0.0.1:8000`

---

## **API Endpoints**

### **1. Get Location Names (for dropdown)**

* **URL:** `/get_location_names`
* **Method:** `GET`
* **Response:**

```json
{
  "locations": ["Indira Nagar", "Whitefield", "Yelahanka", ...]
}
```

---

### **2. Predict Home Price**

* **URL:** `/predict_home_price`

* **Method:** `POST`

* **Form Data Parameters:**

  * `location` (string)
  * `total_sqft` (float)
  * `bhk` (int)
  * `bath` (int)

* **Example using Postman (x-www-form-urlencoded):**

```
location: Indira Nagar
total_sqft: 1000
bhk: 2
bath: 2
```

* **Response:**

```json
{
  "estimated_price": 85.75
}
```

---

## **Notes**

1. Ensure the **artifacts folder** contains the trained model (`decision_tree_model.pkl`) and `columns.json`.
2. If using Postman, select **POST** method and **form-data** for `/predict_home_price`.
3. To exit the virtual environment:

```bash
deactivate
```

---

## **Dependencies**

All dependencies are in `requirements.txt`. Key ones:

* `fastapi`
* `uvicorn`
* `numpy`
* `scikit-learn`
* `pydantic`
* `python-multipart` (for form data)

---

This README gives any developer or user all the information needed to **run your API locally**, use it in **Postman**, or connect it to a **frontend**.

---

