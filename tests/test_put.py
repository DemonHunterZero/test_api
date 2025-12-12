import requests
import time
import pytest

#py -m pytest tests/test_put.py -v para ejecutarlo como prueba
#py -m pytest tests/test_put.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
#py -m pytest -m api -v para ejecutar todas las pruebas api
@pytest.mark.api
def test_put_user(url_base,header_base):
    HEADER = header_base
    URL = f"{url_base}/2" #tbm conocida como endpoint
    PAYLOAD = {"name":"Alan", "job":"Piloto"}

    inicio = time.time() #Toma la hora
    response = requests.put(URL, headers=HEADER, json=PAYLOAD)
    final = time.time() #Toma la hora
    tiempo_tardo = final - inicio

    #Verifica que el recurso sea creado (code: 200)
    assert response.status_code == 200

    #Verifica que la respuesta sea menor a 2 seg
    assert tiempo_tardo < 2, f"La api tardo demasiado {tiempo_tardo}"


    data = response.json()

    assert "updatedAt" in data
    assert isinstance(data["name"], str)

    #Verifica que el nombre de la respuesta sea el mismo que el enviado
    assert data["name"] == PAYLOAD["name"]

