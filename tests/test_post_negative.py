import pytest
from helpers.test_data import TestData


# создание поста без заданных параметров
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
def test_post_posts_without_params(api_handler):
    response = api_handler.post_posts({})
    assert response.status_code == 400, f"Expected status code post posts 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с пустым значением параметра userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.empty_str_params)
def test_post_posts_empty_str_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с None значением параметра userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.none_in_params)
def test_post_posts_none_in_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с пробелом в значении параметра userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.space_in_params)
def test_post_posts_space_in_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с недопустимым типом данных в значении параметра userId, title, body
# в userId строка, в title число, в body число
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.invalid_data_type_in_params)
def test_post_posts_invalid_data_type_in_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с HTML-скриптом в значении параметра userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.html_in_params)
def test_post_posts_html_in_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# создание поста с SQL-инъекцией в значении параметра userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 201 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.sql_in_params)
def test_post_posts_sql_in_param(key, value, api_handler):
    response = api_handler.post_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"