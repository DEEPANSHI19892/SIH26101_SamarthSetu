from pydantic import BaseModel, field_validator
from typing import List, Optional
import bleach

def sanitize(value):
    if value is None:
        return value
    return bleach.clean(value, tags=[], strip=True).strip()

class ProfileResponse(BaseModel):
    name: str
    designation: Optional[str] = None
    department: Optional[str] = None
    jobRole: Optional[str] = None
    experience: Optional[str] = None
    education: Optional[str] = None
    previousTraining: List[str] = []

class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    jobRole: Optional[str] = None
    experience: Optional[str] = None
    education: Optional[str] = None
    previousTraining: Optional[List[str]] = None

    @field_validator("name", "designation", "department", "jobRole", "experience", "education")
    @classmethod
    def clean_text(cls, v):
        return sanitize(v)

    @field_validator("previousTraining")
    @classmethod
    def clean_training(cls, v):
        if v is None:
            return v
        return [sanitize(item) for item in v]