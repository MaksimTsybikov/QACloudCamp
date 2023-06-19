import pytest
from helpers.utils import convert_list_to_dict
from helpers.test_data import TestData


# получение поста по всем несуществующим валидным параметрам
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен 404. "
                          "Убрать mark.xfail, когда починится")
def test_get_posts_with_all_non_existing_params(api_handler):
    response = api_handler.get_posts(TestData.non_existing_post)
    response_dict = convert_list_to_dict(response.json())
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    assert response_dict != TestData.non_existing_post, \
        f"Expected response_dict:{response_dict} equal TestData.non_existing_post{TestData.non_existing_post}"


# получение поста по всем невалидным параметрам
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
def test_get_posts_with_all_invalid_params(api_handler):
    response = api_handler.get_posts(TestData.invalid_params)
    response_dict = convert_list_to_dict(response.json())
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response_dict != TestData.invalid_params, \
        f"Expected response_dict: {response_dict} equal TestData.invalid_params{TestData.invalid_params}"


# получение постов по одному неcуществующему валидному параметру userId, id, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 404."
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.non_existing_post)
def test_get_non_existing_param(key, value, api_handler):
    response = api_handler.get_posts({key: value})
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# получение постов по одному невалидному параметру userId, id, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 400. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.invalid_params)
def test_get_invalid_param(key, value, api_handler):
    response = api_handler.get_posts({key: value})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# получение поста по существующему id и не существующему usedId
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 404 "
                          "Убрать mark.xfail, когда починится")
def test_get_posts_existing_id_non_existing_userid(api_handler):
    response = api_handler.get_posts(TestData.existing_id_non_existing_userid)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"


# получение поста по не существующему id и существующему usedId
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 404 "
                          "Убрать mark.xfail, когда починится")
def test_get_posts_non_existing_id_existing_userid(api_handler):
    response = api_handler.get_posts(TestData.non_existing_id_existing_userid)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    assert response.json() == [], f"Expected response: {response.json()} not equal []"

