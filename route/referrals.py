from fastapi import APIRouter, Body
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["sistercheck"]
inventory_collection = db["inventory"]

# Create the router
router = APIRouter()

@router.post("/referral")
def find_referral(
    missing_items: list[str] = Body(..., embed=True),
    region: str = Body(..., embed=True)
):
    """
    Find hospitals in the same region that have the missing items in stock.
    """
    # Query inventory for the missing items in the specified region with stock > 0
    matches = inventory_collection.find({
        "Region": region,
        "Item": {"$in": missing_items},
        "Available Stock": {"$gt": 0}
    })

    # Organize results by hospital
    hospitals = {}
    for item in matches:
        facility = item.get("Facility")
        item_name = item.get("Item")
        if facility and item_name:
            hospitals.setdefault(facility, []).append(item_name)

    return {"referral_options": hospitals}
