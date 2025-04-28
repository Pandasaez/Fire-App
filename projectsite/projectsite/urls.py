from django.contrib import admin
from django.urls import path

from fire import views
from fire.views import (
    HomePageView, ChartView, 
    PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity,
    PolarAreaData, ScatterChartData, AreaChartData, StackedBarData, MixedChartData
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),

    # original charts
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='line-chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='multi-line-chart'),
    path('multiBarChart/', multipleBarbySeverity, name='multi-bar-chart'),

    # new charts
    path('polarAreaChart/', PolarAreaData, name='polar-area-chart'),
    path('scatterChart/', ScatterChartData, name='scatter-chart'),
    path('areaChart/', AreaChartData, name='area-chart'),
    path('stackedBarChart/', StackedBarData, name='stacked-bar-chart'),
    path('mixedChart/', MixedChartData, name='mixed-chart'),
]
