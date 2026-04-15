Mysuru Public Transport Route Viewer (Django)

A Django-based web application to explore Mysuru public transport routes, stops, and timetables with interactive map visualization.

---

Features

- View all bus routes
- Search routes by number or area
- Detailed route page with:
  - Stops list
  - Timetable
  - Interactive Leaflet map
- Animated bus movement on map
- JSON API endpoint for route data
- Django admin panel for full CRUD:
  - Add / update / delete routes
  - Manage stops and timetables

---

Project Structure

transport/
│── bus_transport/
│   ├── templates/
│   ├── static/
│   │   └── bus_transport/img/bus.png
│   ├── models.py
│   ├── views.py
│   └── urls.py
│── manage.py

---

Tech Stack

- Python 3
- Django
- SQLite
- Leaflet.js
- Bootstrap 5

---

Getting Started

git clone https://github.com/archanabharadwaj18/mysore_transport.git
cd mysore_transport

python -m venv env
env\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

---

Admin Panel

python manage.py createsuperuser

http://127.0.0.1:8000/admin/

---

Map Visualization

- Built using Leaflet.js
- Displays routes with markers and polylines
- Includes animated bus movement

---

API Endpoint

/ api / routes /

---

Author

Archana Bharadwaj
