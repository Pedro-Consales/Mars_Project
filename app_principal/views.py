from django.shortcuts import render, redirect
from app_principal.utils import retorna_forecast
from django.http import JsonResponse
from random import randint


def astronauta_status(request):
    dados = {
        "temperatura_corporal": round(36 + randint(-10, 10)/10, 1),
        "batimento_cardiaco": randint(60, 100),
        "oxigenacao": randint(92, 100)
    }
    return JsonResponse(dados)


def gera_pressao_arterial(request):
    dados = {
        "sistolica": randint(90, 140),
        "diastolica": randint(60, 90)
    }
    return JsonResponse(dados)


def mars_weather_view(request):
    forecasts = retorna_forecast()
    featured_forecast = forecasts[0] if forecasts else None
    regular_forecasts = forecasts[1:] if len(forecasts) > 1 else []
    days = list(range(1, len(forecasts) + 1))

    context = {
        'featured_forecast': featured_forecast,
        'regular_forecasts': regular_forecasts,
        'total_days': len(forecasts),
        'days': days,
        'i': 1,
    }

    return render(request, 'mars_weather.html', context)


def day_detail(request, day_number):
    forecasts = retorna_forecast()

    if day_number < 1 or day_number > len(forecasts):
        return redirect('home/')

    forecast = forecasts[day_number - 1]

    context = {
        'day_number': day_number,
        'forecast': forecast,
        'total_days': len(forecasts),
    }

    return render(request, 'view.html', context)


def user_detail(request):
    context = {}
    return render(request, 'profileview.html', context)