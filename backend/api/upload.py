from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.core.config import recruitment_status
from backend.ai.parser import parse_resume
from backend.ai.groq_agent import process_resume
from backend.ai.writer import append_resume

router = APIRouter()

UPLOAD_FOLDER = Path("backend/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

ALLOWED = [".pdf", ".docx"]


@router.post("/")
async def upload_resume(file: UploadFile = File(...)):

    if not recruitment_status():
        raise HTTPException(
            status_code=403,
            detail="Recruitment Closed"
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    unique_name = f"{uuid.uuid4().hex}{extension}"

    destination = UPLOAD_FOLDER / unique_name

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = parse_resume(str(destination))

    structured = process_resume(text)

    output_file = append_resume(structured)

    # Delete uploaded resume after processing
    try:
        destination.unlink()
    except Exception as e:
        print(f"Could not delete temporary file: {e}")

    return {
        "success": True,
        "candidate": structured.get("name", ""),
        "master_document": output_file
    }