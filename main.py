from fastapi import FastAPI, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from route.referrals import router as referral_router 
from pymongo import MongoClient

app = FastAPI()

# Allow frontend (Flutter) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sistercheck"]
inventory_collection = db["inventory"]

# referrals router
app.include_router(referral_router)


# Root route for sanity check
@app.get("/")
def read_root():
    return {"message": "✅ sistercheck Inventory API is running!"}


# Get full inventory for a hospital
@app.get("/inventory")
def get_inventory(facility: str = Query(..., description="Hospital/Facility name")):
    results = inventory_collection.find({"Facility": facility})
    output = []

    for item in results:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string
        output.append(item)

    return output


# Check treatment availability based on required items
@app.post("/check-treatment-availability")
def check_treatment_availability(
    facility: str = Body(..., embed=True),
    required_items: list[str] = Body(..., embed=True)
):
    # Fetch items available in inventory for this facility
    results = inventory_collection.find({
        "Facility": facility,
        "Item": {"$in": required_items}
    })

    found_items = [item["Item"] for item in results]
    available = list(set(found_items))
    missing = [item for item in required_items if item not in available]

    return {
        "facility": facility,
        "available": available,
        "missing": missing
    }
