import pytest
from helpers.utils import convert_list_to_dict
from helpers.test_data import TestData


# создание поста со всеми валидными несуществующими параметрами
@pytest.mark.xfail(reason="Проблема в API, по-настоящему пост не создается, поэтому найти и удалить его тоже нельзя. "
                          "Убрать mark.xfail, когда починится")
def test_post_posts_with_all_non_existing_params(api_handler):
    response_post = api_handler.post_posts(TestData.related_non_existing_data)
    assert response_post.status_code == 201, f"Expected status code post posts 201, but got {response_post.status_code}"
    # проверить создался ли пост
    response_get = api_handler.get_posts(response_post.json())
    response_get_dict = convert_list_to_dict(response_get.json())
    assert response_get.status_code == 200, f"Expected status code get posts 200, but got {response_get.status_code}"
    # так как посты реально не создаются, то при поиске такого поста падает ошибка
    assert response_get_dict == TestData.related_non_existing_data, \
        f"Expected response_get_dict: {response_get_dict} " \
        f"not equal TestData.related_non_existing_data{TestData.related_non_existing_data}"
    # удалить после создания
    post_id = response_post.json().get("id")
    response_delete = api_handler.delete_posts_with_id(post_id)
    assert response_delete.status_code == 200, \
        f"Expected status code delete posts 200, but got {response_delete.status_code}"
    assert response_delete.json() == {}, f"Expected response: {response_delete.json()} not equal empty object"


# создание поста по одному несуществующему валидному параметру userId, title, body
@pytest.mark.xfail(reason="Проблема в API, по-настоящему пост не создается, поэтому найти и удалить его тоже нельзя. "
                          "Убрать mark.xfail, когда починится")
@pytest.mark.parametrize("key, value", TestData.related_non_existing_params)
def test_post_posts_with_non_existing_param(key, value, api_handler):
    response_post = api_handler.post_posts({key: value})
    assert response_post.status_code == 201, f"Expected status code post posts 201, but got {response_post.status_code}"
    # проверить создался ли пост
    response_get = api_handler.get_posts(response_post.json())
    response_get_dict = convert_list_to_dict(response_get.json())
    assert response_get.status_code == 200, f"Expected status code get posts 200, but got {response_get.status_code}"
    assert response_get_dict == TestData.related_non_existing_params, \
        f"Expected response_get_dict: {response_get_dict} " \
        f"not equal TestData.related_non_existing_params{TestData.related_non_existing_params}"
    # удалить после создания
    post_id = response_post.json().get("id")
    print(post_id)
    response_delete = api_handler.delete_posts_with_id(post_id)
    assert response_delete.status_code == 200, \
        f"Expected status code delete posts 200, but got {response_delete.status_code}"
    assert response_delete.json() == {}, f"Expected response: {response_delete.json()} not equal empty object"
