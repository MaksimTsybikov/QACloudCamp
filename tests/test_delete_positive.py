from helpers.test_data import TestData


# удаление существующего поста по id
def test_delete_posts_with_existing_id(api_handler):
    # создать пост
    response_post = api_handler.post_posts(TestData.related_non_existing_data)
    post_id = response_post.json().get("id")
    assert response_post.status_code == 201, f"Expected status code post posts 201, but got {response_post.status_code}"
    # удалить пост
    response_delete = api_handler.delete_posts_with_id(post_id)
    assert response_delete.status_code == 200, \
        f"Expected status code delete posts 200, but got {response_delete.status_code}"
    assert response_delete.json() == {}, f"Expected response: {response_delete.json()} not equal empty object"
    # проверить, что пост удален
    response_get = api_handler.get_posts_with_id(post_id)
    assert response_get.status_code == 404, f"Expected status code get posts 404, but got {response_get.status_code}"
    assert response_get.json() == {}, f"Expected response: {response_get.json()} not equal []"
