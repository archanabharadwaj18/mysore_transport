from django.contrib import admin
from .models import BusRoute, BusStop, Timetable

class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 1

class TimetableInline(admin.TabularInline):
    model = Timetable
    extra = 1

@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ('route_number', 'start_point', 'end_point')
    search_fields = ('route_number', 'start_point', 'end_point')
    inlines = [BusStopInline, TimetableInline]

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('stop_name', 'route', 'order')
    list_filter = ('route',)
    search_fields = ('stop_name',)

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('route', 'departure_time', 'arrival_time')
    list_filter = ('route',)
    search_fields = ('route__route_number',)


