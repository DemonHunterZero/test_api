import requests
import pytest

#py -m pytest tests/test_post.py -v para ejecutarlo como prueba
#py -m pytest tests/test_post.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
#py -m pytest -m api -v para ejecutar todas las pruebas api
@pytest.mark.api
def test_post_users(url_base,header_base):
    HEADER = header_base
    URL = url_base #tbm conocida como endpoint
    PAYLOAD = {"name":"Alan", "job":"Piloto"}

    response = requests.post(URL, headers=HEADER, json=PAYLOAD)

    #Verifica que el recurso sea creado (code: 201)
    assert response.status_code == 201

    data = response.json()

    #Verifica que el nombre de la respuesta sea el mismo que el enviado
    assert data["name"] == PAYLOAD["name"]

    #Verifica que la respuesta tenga un id
    assert "id" in data

