# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import BusRoute, BusStop, Timetable


def home(request):
    # Simple redirect to route list (or we can show a fancy home page later)
    return route_list(request)


def route_list(request):
    """
    Route List + filtering by route number or area (start/end point).
    """
    query = request.GET.get('q', '')  # can be route number or area text

    routes = BusRoute.objects.all()

    if query:
        routes = routes.filter(
            Q(route_number__icontains=query) |
            Q(start_point__icontains=query) |
            Q(end_point__icontains=query)
        )

    context = {
        "routes": routes,
        "query": query,
    }
    return render(request, "bus_transport/route_list.html", context)


def route_detail(request, route_id):
    """
    Shows one route, its stops and basic timetable.
    """
    route = get_object_or_404(BusRoute, id=route_id)
    stops = route.stops.all()
    timetable = route.timetables.all().order_by("departure_time")

    context = {
        "route": route,
        "stops": stops,
        "timetable": timetable,
    }
    return render(request, "bus_transport/route_detail.html", context)


def timetable_page(request, route_id):
    """
    Dedicated timetable page for a route.
    """
    route = get_object_or_404(BusRoute, id=route_id)
    timetable = route.timetables.all().order_by("departure_time")

    context = {
        "route": route,
        "timetable": timetable,
    }
    return render(request, "bus_transport/timetable.html", context)


def api_routes(request):
    """
    JSON API: expose all routes with stops and timetable.
    """
    routes = BusRoute.objects.all()

    data = []
    for r in routes:
        data.append({
            "route_number": r.route_number,
            "start_point": r.start_point,
            "end_point": r.end_point,
            "stops": [s.stop_name for s in r.stops.all()],
            "timetable": [
                {
                    "departure_time": t.departure_time.strftime("%H:%M"),
                    "arrival_time": t.arrival_time.strftime("%H:%M"),
                }
                for t in r.timetables.all()
            ],
        })

    return JsonResponse(data, safe=False)

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_route_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Create route
        route = BusRoute.objects.create(
            route_number=data["route_number"],
            start_point=data["start"],
            end_point=data["end"]
        )

        # Create stops
        for i, stop in enumerate(data["stops"], start=1):
            BusStop.objects.create(route=route, stop_name=stop, order=i)

        # Create timetable (optional)
        if "timetable" in data:
            for t in data["timetable"]:
                Timetable.objects.create(
                    route=route,
                    departure_time=t["departure"],
                    arrival_time=t["arrival"]
                )

        return JsonResponse({"message": "Route added successfully!"})
    
    return JsonResponse({"error": "POST method only!"})
