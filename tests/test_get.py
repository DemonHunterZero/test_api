import requests
import pytest

#py -m pytest tests/test_get.py -v para ejecutarlo como prueba
#py -m pytest tests/test_get.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
#py -m pytest -m api -v para ejecutar todas las pruebas api
@pytest.mark.api
def test_get_users(url_base, header_base):
    HEADER = header_base
    URL = f"{url_base}?page=2" #tbm conocida como endpoint

    response = requests.get(URL, headers=HEADER)

    #Verifica que el codigo http sea el 200 todo ok
    assert response.status_code == 200

    data = response.json()
    
    #Verifica que en el par llave-valor exista la llave llamada "data"
    assert "data" in data, "No existe la llave data en la respuesta" 

    #Verifica que data sea una lista
    assert isinstance(data["data"], list)

    #Verifica que la lista en la respuesta tenga al menos un elemento o registro
    assert len(data["data"]) > 0