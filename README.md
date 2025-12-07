Mysuru Public Transport Route Viewer — Django Project

A simple Django web application to view bus routes, stops, and timetables for Mysuru public transport.
Includes interactive maps, JSON API, and admin CRUD operations.

🚀 Features

View all bus routes

Search routes by number or area

Route detail page showing:

Stops

Timetable

Interactive Leaflet map

Animated bus movement on map

JSON API endpoint

Django admin panel with:

Add routes

Add stops

Add timetable

Update/Delete routes

📂 Project Structure
transport/
│── bus_transport/
│   ├── templates/
│   ├── static/
│   │   └── bus_transport/img/bus.png
│   ├── models.py
│   ├── views.py
│   └── urls.py
│── manage.py

⚙️ Tech Stack

Python 3

Django

SQLite

Leaflet.js

Bootstrap 5

▶️ How to Run
git clone https://github.com/archanabharadwaj18/mysore_transport.git
cd mysore_transport

python -m venv env
env\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Then open in browser:

http://127.0.0.1:8000/

🔑 Admin Panel

Create superuser:

python manage.py createsuperuser


Login at:

http://127.0.0.1:8000/admin/


You can add:

Routes

Stops

Timetables

All from Django admin.

🗺️ Maps

Leaflet is used to display route lines and moving bus icon.

Bus icon path:

bus_transport/static/bus_transport/img/bus.png

📡 API Endpoint

Get all routes in JSON:

/api/routes/

👩‍💻 Author

Archana Bharadwaj
