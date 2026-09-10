from fastapi import FastAPI
from sqlalchemy import text

from backend.depends import SessionDep

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db")
async def root(session:SessionDep):
    try:
        query = await session.execute(text('SELECT 1'))
        values = query.scalars()
        return {"message": values}
    except Exception as e:
        return {"message": str(e)}

