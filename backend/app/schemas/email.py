from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class EmailResponse(BaseModel):
    category: str