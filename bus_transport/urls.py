from django.urls import path
from . import views

app_name = "bus_transport"

urlpatterns = [
    path("", views.home, name="home"),
    path("routes/", views.route_list, name="route_list"),
    path("routes/<int:route_id>/", views.route_detail, name="route_detail"),
    path("routes/<int:route_id>/timetable/", views.timetable_page, name="timetable_page"),

    # JSON API endpoint
    path("api/routes/", views.api_routes, name="api_routes"),
    path("api/add-route/", views.add_route_api, name="add_route_api"),

]
