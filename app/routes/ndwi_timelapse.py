from fastapi import APIRouter

router = APIRouter(prefix="/timelapse", tags=["timelapse"])

@router.get("/ndwi")
async def ndwi_timelapse():
    """Generate NDWI timelapse (placeholder)."""
    return {"result": "ndwi timelapse"}
