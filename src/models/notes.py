from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
