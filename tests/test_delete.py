import requests
import time
import pytest

#py -m pytest tests/test_delete.py -v para ejecutarlo como prueba
#py -m pytest tests/test_delete.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
#py -m pytest -m api -v para ejecutar todas las pruebas api
@pytest.mark.skip(reason="Desactivada para uso de ejemplo")
def test_delete_users(url_base, header_base):
    HEADER = header_base
    URL = f"{url_base}/2" #tbm conocida como endpoint    

    inicio = time.time() #Toma la hora
    response = requests.delete(URL, headers=HEADER)
    final = time.time() #Toma la hora
    tiempo_tardo = final - inicio

    #Verifica que el recurso sea borrado (code: 204)
    assert response.status_code == 204

    #Verifica que la respuesta sea menor a 2 seg
    assert tiempo_tardo < 2, f"La api tardo demasiado {tiempo_tardo}"


