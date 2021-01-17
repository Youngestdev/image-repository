from pydantic import BaseModel, Field

class UserModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "shopify",
                "password": "shopify123"
            }
        }