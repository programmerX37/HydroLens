from pydantic import BaseModel

class ExampleRequest(BaseModel):
    data: str
