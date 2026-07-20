from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Welcome to vxzktra"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

from app.schemas.email import EmailRequest, EmailResponse
from app.services.email_classifier import classify_email

@router.post("/classify-email", response_model=EmailResponse)
def classify(request: EmailRequest):
    category = classify_email(request.email)

    return EmailResponse(
        category=category
    )