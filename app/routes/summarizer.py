from fastapi import APIRouter
from pydantic import BaseModel
from app.services.summarizer import summarize_text

router = APIRouter()