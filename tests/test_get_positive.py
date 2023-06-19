import pytest
from helpers.utils import convert_list_to_dict
from helpers.test_data import TestData


# получение списка всех постов без параметров
def test_get_posts_without_params(api_handler):
    response = api_handler.get_posts({})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert len(response.json()) > 0, f"Expected length of response: {response.json()} < or = 0"


# получение поста по всем существующим параметрам
def test_get_posts_with_all_existing_params(api_handler):
    response = api_handler.get_posts(TestData.existing_post)
    response_dict = convert_list_to_dict(response.json())
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response_dict == TestData.existing_post, \
        f"Expected response_dict: {response_dict} not equal TestData.existing_post{TestData.existing_post}"


# получение постов по одному существующему параметру userId, id, title, body
@pytest.mark.parametrize("key, value", TestData.unrelated_existing_params)
def test_get_posts_existing_param(key, value, api_handler):
    response = api_handler.get_posts({key: value})
    response_dict = convert_list_to_dict(response.json())
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert (key, value) in response_dict.items(), \
        f"Expected (key, value): {(key, value)} not in response_dict.items(){response_dict.items()}"
