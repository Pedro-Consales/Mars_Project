from django.urls import path
from .views import mars_weather_view, day_detail, user_detail, astronauta_status, gera_pressao_arterial

urlpatterns = [
    path('', mars_weather_view, name='mars_weather'),
    path('dia/<int:day_number>/', day_detail, name='day_detail'),
    path('profile/', user_detail, name='user_detail'),
    path('status-astronauta/', astronauta_status, name='status_astronauta'),
    path('pressao/', gera_pressao_arterial, name='pressao_arterial'),
]