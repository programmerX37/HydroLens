# 🌊 HydroLens: AI-Powered Urban Water Analysis

**HydroLens** is a geospatial intelligence platform for detecting urban flooding and monitoring water body shrinkage using satellite imagery and large language models.

## 🔧 Features

- 📡 Satellite data (NDWI, DEM, LULC) from Google Earth Engine
- 🌊 Waterlogging zone prediction (Bengaluru/Hyderabad)
- 🤖 LLM-based reasoning and query explanations (DeepSeek)
- 🗺️ Interactive frontend with Mapbox + React
- 📈 NDWI timelapse visualizations

## 🚀 Technologies

- Backend: FastAPI + Python
- Frontend: React + Tailwind + Mapbox GL JS
- AI: DeepSeek / LangChain
- Geospatial: Google Earth Engine

For a breakdown of the folder structure see [docs/architecture.md](docs/architecture.md).

## 💻 Development Setup

### Backend

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

HydroLens © 2025 – Built for Bharatiya Antariksh Hackathon 🛰️
