from pydantic import BaseModel,EmailStr
from datetime import datetime

class FitnessClass(BaseModel):
    name:str
    datetime:datetime
    instructor:str
    available_slots:int

class Booking(BaseModel):
    booking_id:int
    class_name: str
    client_name: str
    client_email: str

# For requesting a booking    
class BookingRequest(BaseModel):
    class_name: str
    client_name: str
    client_email: EmailStr
