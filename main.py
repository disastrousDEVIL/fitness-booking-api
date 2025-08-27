from fastapi import FastAPI
from typing import List
from models import FitnessClass, Booking,BookingRequest
from database import decrease_slot, load_classes, load_bookings,save_bookings
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Query
from enum import Enum
import pytz


app=FastAPI(title="Fitness Booking API")


class TimezoneEnum(str, Enum):
    ist = "Asia/Kolkata"
    utc = "UTC"
    new_york = "America/New_York"
    london = "Europe/London"


@app.get("/",response_class=HTMLResponse)
def home():
     return """
    <html>
        <head>
            <title>Fitness Studio Booking API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
                h1 { color: #2c3e50; }
                .card { background: white; padding: 20px; border-radius: 10px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
                code { background: #eee; padding: 2px 6px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>🏋️‍♀️ Fitness Studio Booking API</h1>
            <div class="card">
                <h2>📌 Instructions</h2>
                <ul>
                    <li>1️⃣ View available classes → <code>GET /classes</code></li><br>
                    <li>2️⃣ Make a booking → <code>POST /book</code> (send: class_name, client_name, client_email)</li>
                    <br><li>3️⃣ Check your bookings → <code>GET /bookings?email=your_email@example.com</code></li>
                </ul>
            </div>
            <div class="card">
                <h2>📖 API Docs</h2>
                <ul>
                    <li><a href="/docs">Swagger UI</a></li><br>
                    <li><a href="/redoc">ReDoc</a></li>
                </ul>
            </div>
        </body>
    </html>
    """

@app.get("/classes", response_model=List[FitnessClass])
def get_classes(tz: TimezoneEnum = Query(TimezoneEnum.ist, description="Choose timezone")):
    classes = load_classes()
    try:
        target_tz = pytz.timezone(tz.value)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    for c in classes:
        if c.datetime.tzinfo is None:
            c.datetime = pytz.timezone("Asia/Kolkata").localize(c.datetime)
        c.datetime = c.datetime.astimezone(target_tz)

    return classes
    
@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: str | None = None):
    bookings = load_bookings()
    if email:
        bookings = [b for b in bookings if b.client_email.lower() == email.lower()]
        if not bookings:
            raise HTTPException(status_code=404, detail="No bookings found for this email")
    return bookings

@app.post("/book",response_model=Booking)
def create_booking(request: BookingRequest):
    classes=load_classes()
    bookings=load_bookings()

    fitness_class=None
    for i in classes:
        if i.name.lower()==request.class_name.lower():
            fitness_class=i
            break

    if not fitness_class:
        raise HTTPException(status_code=404,detail="Class not found")
    
    if fitness_class.available_slots==0:
        raise HTTPException(status_code=400,detail="No slots available")
    

    
    decrease_slot(fitness_class)


    new_id=max([b.booking_id for b in bookings],default=0)+1
    new_booking=Booking(booking_id=new_id,
    class_name=fitness_class.name,
    client_name=request.client_name,
    client_email=request.client_email)
    
    bookings.append(new_booking)
    save_bookings(bookings)

    return new_booking

