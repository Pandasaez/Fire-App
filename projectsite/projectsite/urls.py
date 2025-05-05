from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('fireStation_list', FireStationList.as_view(), name='fireStation-list'),
    path('fireStation_list/add', FireStationCreateView.as_view(), name='fireStation-add'),
    path('fireStation_list/<pk>', FireStationUpdateView.as_view(), name='fireStation-update'),
    path('fireStation_list/<pk>/delete', FireStationDeleteView.as_view(), name='fireStation-delete'),
]