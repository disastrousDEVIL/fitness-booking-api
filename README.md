# 🏋️‍♀️ Fitness Studio Booking API

A FastAPI-based REST API for managing fitness class bookings. This API allows users to view available fitness classes, book sessions, and check their booking history.

## ✨ Features

- **View Available Classes**: Get a list of all available fitness classes with real-time slot availability
- **Book Classes**: Reserve slots in fitness classes with email validation
- **Check Bookings**: View booking history by email address
- **Timezone Support**: View class schedules in different timezones
- **Interactive API Documentation**: Built-in Swagger UI and ReDoc documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fitness_booking_api.git
   cd fitness_booking_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```
   
   **Optional: Enable logging for debugging**
   ```bash
   uvicorn main:app --reload --log-level debug
   ```

6. **Access the API**
   - API Homepage: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - ReDoc Documentation: http://localhost:8000/redoc

## 📚 API Endpoints & Sample Requests

### 1. Homepage
**GET** `/` - Welcome page with API instructions

**cURL:**
```bash
curl -X GET "http://localhost:8000/"
```

**Postman:**
- Method: GET
- URL: `http://localhost:8000/`

### 2. Get All Classes
**GET** `/classes` - Get all available fitness classes

**cURL:**
```bash
# Get classes in default timezone (Asia/Kolkata)
curl -X GET "http://localhost:8000/classes"

# Get classes in UTC timezone
curl -X GET "http://localhost:8000/classes?tz=utc"

# Get classes in New York timezone
curl -X GET "http://localhost:8000/classes?tz=new_york"
```

**Postman:**
- Method: GET
- URL: `http://localhost:8000/classes`
- Query Params: `tz` (optional: `ist`, `utc`, `new_york`, `london`)

**Sample Response:**
```json
[
    {
        "name": "Yoga",
        "datetime": "2025-08-28T07:00:00+05:30",
        "instructor": "Priya Sharma",
        "available_slots": 1
    },
    {
        "name": "Zumba",
        "datetime": "2025-08-28T18:00:00+05:30",
        "instructor": "Rahul Verma",
        "available_slots": 10
    }
]
```

### 3. Get All Bookings
**GET** `/bookings` - Get all bookings

**cURL:**
```bash
curl -X GET "http://localhost:8000/bookings"
```

**Postman:**
- Method: GET
- URL: `http://localhost:8000/bookings`

### 4. Get Bookings by Email
**GET** `/bookings?email={email}` - Filter bookings by client email

**cURL:**
```bash
curl -X GET "http://localhost:8000/bookings?email=test@example.com"
```

**Postman:**
- Method: GET
- URL: `http://localhost:8000/bookings`
- Query Params: `email=test@example.com`

**Sample Response:**
```json
[
    {
        "booking_id": 2,
        "class_name": "Yoga",
        "client_name": "test User",
        "client_email": "test@example.com"
    }
]
```

### 5. Create a Booking
**POST** `/book` - Create a new booking

**cURL:**
```bash
curl -X POST "http://localhost:8000/book" \
  -H "Content-Type: application/json" \
  -d '{
    "class_name": "Yoga",
    "client_name": "John Doe",
    "client_email": "john@example.com"
  }'
```

**Postman:**
- Method: POST
- URL: `http://localhost:8000/book`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
    "class_name": "Yoga",
    "client_name": "John Doe",
    "client_email": "john@example.com"
}
```

**Sample Response:**
```json
{
    "booking_id": 6,
    "class_name": "Yoga",
    "client_name": "John Doe",
    "client_email": "john@example.com"
}
```

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
pytest test_main.py -v
```

**Expected Test Output:**
```
test_main.py::test_root_endpoint PASSED
test_main.py::test_get_classes PASSED
test_main.py::test_post_bookings PASSED
test_main.py::test_get_bookings PASSED
```

## 📁 Project Structure

```
fitness_booking_api/
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic models for data validation
├── database.py          # Data persistence layer
├── test_main.py         # Test suite
├── requirements.txt     # Python dependencies
├── data/               # JSON data files
│   ├── classes.json    # Fitness classes data
│   └── bookings.json   # Bookings data
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── LICENSE             # MIT License
```

## 📊 Sample Data

### Classes Data (`data/classes.json`)
The application comes with sample fitness classes:
- **Yoga** with Priya Sharma (1 slot available)
- **Zumba** with Rahul Verma (10 slots available)
- **HIIT** with Neha Singh (14 slots available)

### Bookings Data (`data/bookings.json`)
Sample bookings are included to demonstrate the API functionality.

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework
- **Uvicorn**: ASGI server for running FastAPI applications (with built-in logging support)
- **Pytz**: Timezone handling

## 🔧 API Features

### Data Validation
- Email validation for booking requests
- Class name validation against available classes
- Slot availability checking

### Error Handling
- 404 errors for non-existent classes
- 400 errors for unavailable slots
- Proper HTTP status codes and error messages

### Timezone Support
- View class schedules in different timezones
- Supported timezones: IST, UTC, New York, London

## 🎯 Demo Scenarios

### Scenario 1: View Available Classes
1. Start the server: `uvicorn main:app --reload` (or `uvicorn main:app --reload --log-level debug` for detailed logs)
2. Visit: http://localhost:8000/docs
3. Try the `/classes` endpoint
4. Test different timezone parameters

### Scenario 2: Book a Class
1. Use the `/book` endpoint
2. Try booking "Yoga" class
3. Verify the slot count decreases
4. Check bookings with `/bookings` endpoint

### Scenario 3: Check Bookings by Email
1. Use `/bookings?email=test@example.com`
2. Verify only bookings for that email are returned

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/yourusername/fitness_booking_api/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide detailed information about your problem

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Payment integration
- [ ] Email notifications
- [ ] Class cancellation functionality
- [ ] Waitlist management
- [ ] Instructor management
- [ ] Analytics and reporting

