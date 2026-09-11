from pydantic import BaseModel, ConfigDict


class GetHabitSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_tg_id: int
    habit: str
    unit: str
    count: int

class CreateHabitSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_tg_id: int
    habit: str
    unit: str
    count: int


