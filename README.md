# SisterCheck Inventory API

This backend service was developed as part of the **SisterCheck** project during the [Hackathon Name or Event, e.g. "2025 HealthTech Innovation Hackathon"].  
It provides a lightweight **FastAPI + MongoDB** backend for managing hospital inventory data and checking treatment item availability across facilities.

---

## 💡 Overview

The **Inventory API** enables healthcare facilities to:
- Upload resource inventory data directly from Excel sheets.
- Query their available medical resources by facility.
- Check whether a treatment can be supported based on required items.

This module was designed and implemented as the **inventory and data integration component** of the SisterCheck system.

---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Backend Framework | FastAPI |
| Database | MongoDB |
| Data Upload | Python (Pandas) |
| API Middleware | CORS (for Flutter frontend integration) |

---

## 🧩 My Role (Individual Contribution)

During the hackathon, I was responsible for:
- Designing and implementing the **FastAPI backend** for the inventory system.  
- Integrating **MongoDB** for efficient storage and retrieval of resource data.  
- Developing the **Excel-to-MongoDB upload script** using `pandas`.  
- Creating API endpoints for:
  - Fetching a hospital's full inventory.
  - Checking treatment availability based on required resources.
- Enabling CORS to allow the **Flutter frontend** to consume the API securely.

---

## 📁 Project Structure

