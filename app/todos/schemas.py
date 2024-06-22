from pydantic import BaseModel, ConfigDict
from datetime import date

class SchemaCreateTodo(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    title: str = "Todo"
    description: str = "Description"
    deadline: date

class SchemaUpdateTodo(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    title: str
    description: str
    deadline: date
