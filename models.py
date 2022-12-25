from pydantic import BaseModel

class Argument(BaseModel):    
    sex: int
    age: int
    sib_count: int
    pclass: int

class ArgumentResponse(BaseModel):
    survive: str
    proba: float