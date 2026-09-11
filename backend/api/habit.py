from typing import List, Tuple, Sequence

from fastapi import APIRouter, HTTPException

from backend.schema import HabitSchema

from backend.depends import SessionDep

from backend.model.HabitModel import HabitModel

from sqlalchemy import Select

from backend.schema.HabitSchema import CreateHabitSchema, GetHabitSchema

router = APIRouter()
tag = 'habit'

@router.get('/habit',summary='получить все привычки', tags=[tag])
async def get_all_habits(session:SessionDep):
    query = Select(HabitModel)
    result = await session.execute(query)
    if result.fetchone() is None:
        raise HTTPException(status_code=404,detail='habitat not found')
    return result.scalars().all()

@router.get('/habit/habit_id', summary='получить конкретную привычку', tags=[tag])
async def get_habit_by_id(session:SessionDep,habit_id:int) -> GetHabitSchema:
    query = Select(HabitModel).where(HabitModel.id == habit_id)
    result = await session.execute(query)
    if result.scalar() is None:
        raise HTTPException(status_code=404,detail='habit not found')
    return result.scalars().one()

@router.post('/habit', summary='создание привычки', tags=[tag])
async def create_habit(habit:CreateHabitSchema, session:SessionDep) -> GetHabitSchema:
    try:
        new_habit = HabitModel(**habit.dict())
        session.add(new_habit)
        await session.commit()
        await session.refresh(new_habit)
        return GetHabitSchema.model_validate(new_habit)
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


