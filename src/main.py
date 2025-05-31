from fastapi import FastAPI
from router import notes
from db.database import engine
from models import notes as notes_model

# Create table
notes_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API with PostgreSQL")

# Register Routers
app.include_router(notes.router)