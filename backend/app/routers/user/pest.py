from fastapi import APIRouter, UploadFile, File
from app.schemas.pest import PestResult
from app.schemas.common import Source

router = APIRouter()

@router.post("/image/pest", response_model=PestResult)
async def classify_pest(image: UploadFile = File(...)) -> PestResult:
    # Mock classification regardless of input image
    return PestResult(
        pest_name="Brown planthopper",
        severity="Moderate",
        treatment_steps=[
            "Reduce nitrogen application; drain field for 3–4 days.",
            "Apply recommended insecticide as per ICAR guidance.",
        ],
        sources=[Source(title="ICAR Rice Pests Guide", excerpt="Planthopper control")],
        confidence=76,
    )