from fastapi import APIRouter

router = APIRouter(prefix="/waterlogging", tags=["waterlogging"])

@router.get("/{city}")
async def get_waterlogging(city: str):
    """Return waterlogging info for the given city."""
    return {"city": city, "status": "placeholder"}
