import json
from typing import List
from models import FitnessClass, Booking

CLASSES_FILE = "data/classes.json"
BOOKING_FILE = "data/bookings.json"


def load_classes() -> List[FitnessClass]:
    try:
        with open(CLASSES_FILE,"r") as f:
            data=json.load(f)
            return [FitnessClass(**item) for item in data]
    except FileNotFoundError:
        return []

def decrease_slot(class1: FitnessClass):
   
    with open(CLASSES_FILE, "r") as f:
        data = json.load(f)

   
    for i in data:
        if i['name'].lower() == class1.name.lower():
            i['available_slots'] -= 1
            break

  
    with open(CLASSES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_bookings() -> List[Booking]:
    try:
        with open(BOOKING_FILE,"r") as t:
            data=json.load(t)
            return [Booking(**item) for item in data]
    except FileNotFoundError:
        return []


def save_bookings(bookings:List[Booking]):
    with open(BOOKING_FILE,"w") as t:
        json.dump([b.model_dump() for b in bookings],t,indent=4)