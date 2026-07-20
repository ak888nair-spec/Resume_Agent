from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.download import router as download_router
from backend.api.admin import router as admin_router
from backend.api.upload import router as upload_router

app = FastAPI(
    title="Resume Automation",
    version="1.0.0",
    description="AI Resume Automation Backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(download_router, prefix="/download", tags=["Download"])

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Resume Automation Backend"
    }


@app.get("/health")
def health():
    return {
        "backend": "online"
    }