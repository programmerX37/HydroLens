from fastapi import APIRouter

router = APIRouter(prefix="/prompt", tags=["prompt"])

@router.post("")
async def run_prompt():
    """Interact with the language model (placeholder)."""
    return {"message": "prompt response"}
