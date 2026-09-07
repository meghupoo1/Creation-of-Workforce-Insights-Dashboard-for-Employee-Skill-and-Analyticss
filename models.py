from datetime import date
from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
	id: int
	title: str
	date: date
	organizer: Optional[str] = None
	city: str = "Bangalore"
	email: Optional[str] = None
