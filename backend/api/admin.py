import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.core.config import (
    recruitment_status,
    set_recruitment
)

load_dotenv()

router = APIRouter()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

logged_in = False


class LoginRequest(BaseModel):
    password: str


@router.post("/login")
def login(data: LoginRequest):

    global logged_in

    if data.password == ADMIN_PASSWORD:

        logged_in = True

        return {
            "success": True
        }

    raise HTTPException(
        status_code=401,
        detail="Incorrect Password"
    )


def verify_admin():

    if not logged_in:

        raise HTTPException(
            status_code=401,
            detail="Administrator Login Required"
        )


@router.post("/recruit/open")
def open_recruitment():

    verify_admin()

    set_recruitment(True)

    return {
        "success": True,
        "message": "Recruitment Opened"
    }


@router.post("/recruit/close")
def close_recruitment():

    verify_admin()

    set_recruitment(False)

    return {
        "success": True,
        "message": "Recruitment Closed"
    }


@router.get("/recruit/status")
def status():

    return {
        "recruitment": recruitment_status()
    }