from fastapi import FastAPI, HTTPException
from typing import List
from models import Event
from datetime import date

proj = FastAPI(title="AI Event Assistant 2")

events_db: List[Event] = [
    Event(
        id=1,
        title="AI Bootcamp",
        date="2025-10-24",
        organizer="Tech Club",
        city="Bangalore",
        email="techclub@example.com"
    ),
    Event(
        id=2,
        title="Python Workshop",
        date="2025-11-05",
        organizer="Coding Club",
        city="Bangalore",
        email="coding@example.com"
    ),
    Event(
        id=3,
        title="Cloud Computing Seminar",
        date="2025-11-15",
        organizer="IT Department",
        city="Mysore",
        email="it@example.com"
    )
]


# Create an event
@proj.post("/events/add")
def create_event(
    event_id: int,
    title: str,
    date: date = date.today(),
    organizer: str = None,
    email: str = None,
    city: str = "Bangalore"
):
    for event in events_db:
        if event.id == event_id:
            return {
                "ERROR!!!": f"Event with id {event_id} already exists!!!"
            }

    event = Event(
        id=event_id,
        title=title,
        date=date,
        organizer=organizer,
        city=city,
        email=email
    )

    events_db.append(event)

    return {
        "message": "Event created successfully",
        "event": event
    }


# Fetch all events
@proj.get("/events")
def get_all_events():
    return events_db


# Search events by title and city
@proj.get("/events/search")
def search_events(
    title: str,
    city: str = "Bangalore"
):
    result = []

    for event in events_db:
        if (
            event.title.lower() == title.lower()
            and event.city.lower() == city.lower()
        ):
            result.append(event)

    return result