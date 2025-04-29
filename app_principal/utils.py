import requests
from datetime import datetime, timedelta
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()


class Forecast:
    def __init__(self, solHoje, avgTemperature, maxTemperature, minTemperature, avgWind_speed, maxWind_speed, minWind_speed, wind_direction, avgAtmospheric_pressure, maxAtmospheric_pressure, minAtmospheric_pressure, season, storm_warning,indicieUV):
        
        self.solHoje = solHoje

        self.avgTemperature = avgTemperature
        self.maxTemperature = maxTemperature
        self.minTemperature = minTemperature

        self.avgWind_speed = avgWind_speed
        self.maxWind_speed = maxWind_speed
        self.minWind_speed = minWind_speed

        self.wind_direction = wind_direction

        self.avgAtmospheric_pressure = avgAtmospheric_pressure
        self.maxAtmospheric_pressure = maxAtmospheric_pressure
        self.minAtmospheric_pressure = minAtmospheric_pressure

        self.season = season

        self.storm_warning = storm_warning

        self.indicieUV = indicieUV


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def mps_to_kmh(mps):
    return mps * 3.6

def obtemSolAtual(dataAtual):
    solZero = datetime(2018,11,26)
    duracaoSol = timedelta(hours=24, minutes=39)

    diferenca = dataAtual - solZero  # timedelta
    solAtual = diferenca.total_seconds() / duracaoSol.total_seconds()
    
    return int(solAtual)



direcoes_pt = {
    "N": "Norte",
    "NNE": "Norte-nordeste",
    "NE": "Nordeste",
    "ENE": "Leste-nordeste",
    "E": "Leste",
    "ESE": "Leste-sudeste",
    "SE": "Sudeste",
    "SSE": "Sul-sudeste",
    "S": "Sul",
    "SSW": "Sul-sudoeste",
    "SW": "Sudoeste",
    "WSW": "Oeste-sudoeste",
    "W": "Oeste",
    "WNW": "Oeste-noroeste",
    "NW": "Noroeste",
    "NNW": "Norte-noroeste"
}



def retorna_forecast():


    mars_token = os.getenv("MARS_TOKEN")

    url = f"https://api.nasa.gov/insight_weather/?api_key={mars_token}&feedtype=json&ver=1.0"

    response = requests.get(url)

    data = response.json()

    sols = data.get("sol_keys", [])

    listaForecast = []

    j = 0

    if not sols:

        return forecast

    else:

        for i in range(0, (len(sols)-1)):

            solAtual = sols[i]
            dados_solAtual = data[solAtual]

            #---- 
            #Obtem os dados de temperatura do sol atual
            tempAtualMediaF = dados_solAtual.get("AT", {}).get("av", {})
            tempAtualMediaC = fahrenheit_to_celsius(tempAtualMediaF)

            tempMaximaF = dados_solAtual.get("AT",{}).get("mx", {})
            tempMaximaC = fahrenheit_to_celsius(tempMaximaF)

            tempMinimaF = dados_solAtual.get("AT",{}).get("mn",{})
            tempMinimaC = fahrenheit_to_celsius(tempMinimaF)

            #----
            #Obtem os dados de vento do sol atual
            velMediaVento_MpS = dados_solAtual.get("HWS",{}).get("av", {})
            velMediaVento_KmH = mps_to_kmh(velMediaVento_MpS)

            velMaxVento_MpS = dados_solAtual.get("HWS",{}).get("mx", {})
            velMaxVento_KmH = mps_to_kmh(velMaxVento_MpS)

            velMinimaVento_MpS = dados_solAtual.get("HWS",{}).get("mn", {})
            velMinimaVento_KmH = mps_to_kmh(velMinimaVento_MpS)


            #----
            #Obtem direção do vento do sol atual
            direcaoVento = dados_solAtual.get("WD",{}).get("most_common", {}).get("compass_point", "")
            direcaoVento_PT = direcoes_pt.get(direcaoVento, "")

            #----
            #Obtem pressão do sol atual
            pressaoMediaAtmosferica = dados_solAtual.get("PRE",{}).get("av", {})

            pressaoMaximaAtmosferica = dados_solAtual.get("PRE",{}).get("mx", {})
            pressaoMinimaAtmosferica = dados_solAtual.get("PRE",{}).get("mn", {})


            #----
            #Obtem a season do sol atual
            estacaoDoAno = dados_solAtual.get("Season", [])
            

            difAtm = pressaoMaximaAtmosferica - pressaoMinimaAtmosferica
            difTemp = tempMaximaC - tempMinimaC
            
            storm_warning = 0

             # Verifica as condições para alta possibilidade de tempestade
            if velMaxVento_KmH >= 90 and difAtm >= 100 and difTemp >= 100:
                storm_warning = 3

            # Verifica as condições para média possibilidade de tempestade
            elif 70 <= velMaxVento_KmH < 90 and 40 <= difAtm < 100 and 40 <= difTemp < 100:
                storm_warning = 2

            # Caso contrário, baixa possibilidade de tempestade
            else:
                storm_warning = 1
                
            diaAtual = datetime.now()

            indicieUV = randint(5, 20)  # Simulando um índice UV aleatório entre 5 e 20


            solHoje = obtemSolAtual(diaAtual)+j

            j += 1
            #----
            #Cria o Forecast
            forecast = Forecast(solHoje,tempAtualMediaC, tempMaximaC, tempMinimaC, velMediaVento_KmH, velMaxVento_KmH, velMinimaVento_KmH, direcaoVento_PT, pressaoMediaAtmosferica, pressaoMaximaAtmosferica, pressaoMinimaAtmosferica, estacaoDoAno, storm_warning, indicieUV)
            
            listaForecast.append(forecast)

    return listaForecast





    