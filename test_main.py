from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Fitness Studio Booking API" in response.text

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  
    # Now we checked it should be a list but it should be a list of dictionaries right?
    first_class = data[0]
    assert isinstance(first_class, dict)   # each item is a dict
    assert "name" in first_class
    assert "datetime" in first_class
    assert "instructor" in first_class
    assert "available_slots" in first_class

def test_post_bookings():
    payload = {
        "class_name": "Yoga",
        "client_name": "test User",
        "client_email": "test@example.com"
    }
    response = client.post("/book", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['class_name'] == "Yoga"
    assert data['client_email'] == "test@example.com"

def test_get_bookings():
    # Step 1: Create a booking
    client.post("/book", json={
        "class_name": "Yoga",
        "client_name": "Booking Tester",
        "client_email": "tester@example.com"
    })

    # Step 2: Check bookings for that email
    response = client.get("/bookings?email=tester@example.com")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["client_email"] == "tester@example.com"
