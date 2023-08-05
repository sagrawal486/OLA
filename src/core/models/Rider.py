from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Extra

class Rider(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    