# 🏋️‍♀️ Fitness Studio Booking API

A lightweight **FastAPI REST service** for managing fitness studio operations — enabling users to browse classes, reserve slots, and track their bookings.  
Built as part of a Python Developer Assignment to demonstrate backend API design, validation, modularity, and testing.

---

## 🚀 Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/fitness_booking_api.git
   cd fitness_booking_api
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the server

   ```bash
   uvicorn main:app --reload
   ```

👉 API will be available at:

* Homepage: [http://localhost:8000/](http://localhost:8000/)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📝 Logging

By default, Uvicorn prints logs to the console.
To save logs (including errors) into a file, run:

```bash
uvicorn main:app --reload > logs.txt 2>&1
```

* `> logs.txt` → saves standard output logs
* `2>&1` → saves error logs into the same file

👉 Check logs at any time:

```bash
type logs.txt   # Windows
cat logs.txt    # Linux/Mac
```

---

## 📚 API Endpoints

### 🔹 1. API Status

**GET /**
Returns an HTML page with instructions and links to `/docs` and `/redoc`.

```bash
curl http://localhost:8000/
```

---

### 🔹 2. Get Classes (with Timezone Support)

**GET /classes**
Returns all available fitness classes.

Supports optional query parameter `tz` to convert class timings into a specific timezone.

**Supported values (dropdown in Swagger UI):**

* `Asia/Kolkata` (default IST)
* `UTC`
* `America/New_York`
* `Europe/London`

```bash
curl http://localhost:8000/classes
curl "http://localhost:8000/classes?tz=UTC"
curl "http://localhost:8000/classes?tz=America/New_York"
```

✅ Example Response:

```json
[
  {
    "name": "Yoga",
    "datetime": "2025-08-28T01:30:00+00:00",
    "instructor": "Priya Sharma",
    "available_slots": 10
  }
]
```

---

### 🔹 3. Get All Bookings

**GET /bookings**
Returns all bookings.

```bash
curl http://localhost:8000/bookings
```

---

### 🔹 4. Get Bookings by Email

**GET /bookings?email=...**
Filters bookings for a specific client email. Returns 404 if no bookings found.

```bash
curl "http://localhost:8000/bookings?email=test@example.com"
```

✅ Example Response:

```json
[
  {
    "booking_id": 1,
    "class_name": "Yoga",
    "client_name": "Alice",
    "client_email": "alice@example.com"
  }
]
```

---

### 🔹 5. Create a Booking

**POST /book**
Books a slot in a class, reduces available slots, and saves the booking.

```bash
curl -X POST http://localhost:8000/book \
  -H "Content-Type: application/json" \
  -d '{"class_name":"Yoga","client_name":"John","client_email":"john@example.com"}'
```

✅ Example Response:

```json
{
  "booking_id": 2,
  "class_name": "Yoga",
  "client_name": "John",
  "client_email": "john@example.com"
}
```

❌ Error cases:

* `404` → Class not found
* `400` → No slots available
* `422` → Invalid email format

---

## 📦 Sample Data

### `data/classes.json`

```json
[
  {
    "name": "Yoga",
    "datetime": "2025-08-28T07:00:00+05:30",
    "instructor": "Priya Sharma",
    "available_slots": 10
  },
  {
    "name": "Zumba",
    "datetime": "2025-08-28T18:00:00+05:30",
    "instructor": "Rahul Verma",
    "available_slots": 15
  },
  {
    "name": "HIIT",
    "datetime": "2025-08-29T06:30:00+05:30",
    "instructor": "Neha Singh",
    "available_slots": 12
  }
]
```

### `data/bookings.json`

```json
[]
```

---

## 🧪 Testing

Unit tests are written using **pytest**.

Run the test suite:

```bash
pytest -v
```

### Included Tests

* ✅ Root `/` endpoint loads successfully
* ✅ `/classes` returns a list of dictionaries with correct keys
* ✅ `/book` creates a booking successfully
* ✅ `/bookings?email=...` returns correct booking

---

## 🔮 Future Enhancements

* [ ] Switch JSON file storage → SQLite/PostgreSQL
* [ ] Add user authentication & role-based access
* [ ] Enable payments & email notifications
* [ ] Instructor & class management dashboard

---

## 📄 License

MIT License – free to use and modify.



