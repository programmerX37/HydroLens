from fastapi import FastAPI

from .routes import waterlogging, ndwi_timelapse, analyze, prompt

app = FastAPI(title="HydroLens API")

app.include_router(waterlogging.router)
app.include_router(ndwi_timelapse.router)
app.include_router(analyze.router)
app.include_router(prompt.router)

@app.get("/")
async def root():
    return {"message": "Welcome to HydroLens"}
