import pytest
from helpers.test_data import TestData


# удаление несуществующего поста по валидному id
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, а должен быть 404. "
                          "Убрать mark.xfail, когда починится")
def test_delete_posts_with_non_existing_id(api_handler):
    response = api_handler.delete_posts_with_id(TestData.non_existing_id)
    assert response.status_code == 404, \
        f"Expected status code delete posts 404, but got {response.status_code}"
    assert response.json() == {}, f"Expected response: {response.json()} not equal empty object"


# удаление поста по невалидному id
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код и 404 на кейс с пустой строкой, "
                          "убрать mark.xfail, когда починится")
@pytest.mark.parametrize("value", TestData.not_valid_id)
def test_delete_posts_with_not_valid_id(value, api_handler):
    response = api_handler.delete_posts_with_id(value)
    assert response.status_code == 400, \
        f"Expected status code delete posts 400, but got {response.status_code}"
    assert response.json() == {}, f"Expected response: {response.json()} not equal empty object"


# удаления постов по существующим значениям параметров id, userId, title, body
@pytest.mark.xfail(reason="Проблема в API, возвращается 404 код, хотя должен 400 Bad request"
                          "убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.unrelated_existing_params)
def test_delete_posts_with_existing_param(key, value, api_handler):
    response = api_handler.delete_posts_with_params({key: value})
    assert response.status_code == 400, \
        f"Expected status code delete posts 400, but got {response.status_code}"
    assert response.json() == {}, f"Expected response: {response.json()} not equal empty object"


# удаление поста без id
@pytest.mark.xfail(reason="Проблема в API, возвращается 200 код, хотя должен 400 Bad request"
                          "убрать mark.xfail, когда починится")
def test_delete_posts_without_id(api_handler):
    response = api_handler.delete_posts_with_id(None)
    assert response.status_code == 400, \
        f"Expected status code delete posts 400, but got {response.status_code}"
    assert response.json() == {}, f"Expected response: {response.json()} not equal empty object"
