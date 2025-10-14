from fastapi import FastAPI
from database import engine, Base
from Eusers.router import user_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

