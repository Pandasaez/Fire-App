from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation


class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"

def map_station(request):  
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')  

    for fs in fireStations:  
        fs['latitude'] = float(fs['latitude'])  
        fs['longitude'] = float(fs['longitude'])  

    fireStations_list = list(fireStations)  

    context = {  
        'fireStations': fireStations_list,  
    }  

    return render(request, 'map_station.html', context)  

def map_incident(request):
    # Get all relevant fields INCLUDING city
    incidents = Locations.objects.values('name', 'latitude', 'longitude', 'city')

    for fs in incidents:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])

    # Collect unique cities for the dropdown filter
    cities = Locations.objects.values_list('city', flat=True).distinct()

    incident_list = list(incidents)
    city_list = list(cities)

    context = {
        'incident': incident_list,
        'cities': city_list,  # Pass cities to template
    }

    return render(request, 'map_incidents.html', context)


