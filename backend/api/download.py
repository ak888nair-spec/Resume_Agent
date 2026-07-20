from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import HTTPException

router = APIRouter()

MASTER_FILE = Path("backend/output/MasterResume.docx")


@router.get("/")
def download_master_resume():

    if not MASTER_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="No resumes have been processed yet."
        )

    return FileResponse(
        path=MASTER_FILE,
        filename="MasterResume.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )