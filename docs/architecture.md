# Project Architecture

This project is split into backend and frontend components along with
supporting datasets, notebooks, and documentation. Below is an overview of the
main directories.

```
HydroLens/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── app/                    # FastAPI backend
│   ├── main.py             # Entry point
│   ├── routes/             # API route modules
│   ├── utils/              # Geospatial and AI helpers
│   └── models/             # Pydantic schemas
├── frontend/               # React + Tailwind frontend
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   └── utils/
│   ├── tailwind.config.js
│   └── package.json
├── data/                   # Example datasets
│   ├── raw/                # Downloaded GEE data
│   ├── processed/          # Cleaned rasters or geojson
│   └── samples/            # Example NDWI plots
├── notebooks/              # Jupyter analyses
├── docs/                   # Additional documentation
│   ├── architecture.md
│   ├── api_reference.md
│   └── usage_guide.md
```

Each submodule is kept small and focused to make it easy to contribute or
extend the application.
